from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forum.models import Post, Comment
from .models import Profiler
from .forms import ProfilerForm


@login_required
def profiler_page(request):
    """
    Display and handle updates to the user's profile page.
    Retrieves or creates a profile for the logged-in user and displays their
    latest posts and comments. Handles profile updates through POST requests.
    """
    user = request.user
    try:
        profiler = Profiler.objects.get(profile_user=user)
    except Profiler.DoesNotExist:
        profiler = Profiler.objects.create(profile_user=user)

    profiler.profile_last_posts.set(
        Post.objects.filter(post_author=user)
        .order_by('-post_created_on')[:3]
    )
    profiler.profile_last_comments.set(
        Comment.objects.filter(comment_author=user)
        .order_by('-comment_created_on')[:3]
    )
    profiler.save()

    if request.method == "POST":
        profiler_form = ProfilerForm(data=request.POST, instance=profiler)
        if profiler_form.is_valid():
            profiler_form.save()
            messages.success(request, "Profile Edited and Saved")
            return HttpResponseRedirect(reverse("profiler"))
    else:
        profiler_form = ProfilerForm(instance=profiler)

    return render(
        request,
        "profiler/profiler.html",
        {
            "profiler": profiler,
            'profiler_form': profiler_form,
            "is_owner": True,
        },
    )


@login_required
def profiler_edit(request, profiler_id):
    """
    Handle detailed profile editing.
    Allows users to edit their profile details including uploaded files.
    Only accessible to the profile owner.
    """
    profiler = get_object_or_404(
        Profiler,
        id=profiler_id,
        profile_user=request.user
    )

    if request.method == "POST":
        profiler_form = ProfilerForm(
            request.POST,
            request.FILES,
            instance=profiler
        )
        if profiler_form.is_valid():
            profiler_form.save()
            messages.success(request, 'Profile Updated!')
            return HttpResponseRedirect(reverse("profiler"))
        messages.error(request, 'Error updating profile!')
    else:
        profiler_form = ProfilerForm(instance=profiler)

    return render(
        request,
        "profiler/profiler_editor.html",
        {
            'profiler_form': profiler_form,
            'profiler': profiler
        },
    )


@login_required
def profile_delete(request, pk):
    """
    Handle profile and user account deletion.

    Allows users to delete their profile and associated account.
    Requires confirmation through POST request.
    """
    profiler = get_object_or_404(
        Profiler,
        pk=pk,
        profile_user=request.user
    )

    if request.user != profiler.profile_user:
        messages.error(request, 'You can only delete your own profile.')
        return redirect('profiler')

    if request.method == 'POST':
        user = profiler.profile_user
        user.delete()
        messages.success(
            request,
            'Your account and all associated data have been deleted.'
        )
        return redirect('home')

    context = {
        'profiler': profiler,
        'post_count': Post.objects.filter(post_author=request.user).count(),
        'comment_count': Comment.objects.filter(comment_author=request.user).count(),
    }
    return render(request, 'profiler/profiler_deletor.html', context)


def view_profile(request, username):
    """
    View a user's profile page.
    Displays profile information for any user, while restricting edit access
    to profile owners only.
    """
    user = get_object_or_404(User, username=username)
    profiler = get_object_or_404(Profiler, profile_user=user)
    
    profiler.profile_last_posts.set(
        Post.objects.filter(post_author=user)
        .order_by('-post_created_on')[:3]
    )
    profiler.profile_last_comments.set(
        Comment.objects.filter(comment_author=user)
        .order_by('-comment_created_on')[:3]
    )
    profiler.save()

    return render(
        request,
        "profiler/profiler.html",
        {
            "profiler": profiler,
            "is_owner": request.user == user if request.user.is_authenticated else False,
        },
    )
