from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forum.models import Post, Comment
from .models import Profiler
from .forms import ProfilerForm


@login_required
def profiler_page(request):
    """
    Renders the Profiler page
    """
    user = request.user

    try:
        profiler = Profiler.objects.get(profile_user=user)
    except Profiler.DoesNotExist:
        profiler = Profiler.objects.create(profile_user=user)

    profiler.profile_last_posts.set(Post.objects.filter(post_author=user).order_by('-post_created_on')[:3])
    profiler.profile_last_comments.set(Comment.objects.filter(comment_author=user).order_by('-comment_created_on')[:3])
    profiler.save()

    profiler_form = ProfilerForm(instance=profiler)
    if request.method == "POST":
        profiler_form = ProfilerForm(data=request.POST, instance=profiler)
        if profiler_form.is_valid():
            profiler_form.save()
            messages.success(request, "Profile Edited and Saved")
            return HttpResponseRedirect(reverse("profiler"))

    return render(
        request,
        "profiler/profiler.html",
        {
            "profiler": profiler,
            'profiler_form': profiler_form,
        },
    )

@login_required 
def profiler_edit(request, profiler_id):
    """
    View to edit the profiler
    """
    profiler = get_object_or_404(Profiler, id=profiler_id, profile_user=request.user)

    if request.method == "POST":
        profiler_form = ProfilerForm(request.POST, request.FILES, instance=profiler)
        if profiler_form.is_valid():
            profiler_form.save()
            messages.success(request, 'Profile Updated!')
            return HttpResponseRedirect(reverse("profiler"))
        else:
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
    View to delete a profile
    """
    profiler = get_object_or_404(Profiler, pk=pk, profile_user=request.user)
    
    if request.user != profiler.profile_user:
        messages.error(request, 'You can only delete your own profile.')
        return redirect('profiler')
    
    if request.method == 'POST':
        user = profiler.profile_user
        user.delete()
        
        messages.success(request, 'Your account and all associated data have been deleted.')
        return redirect('home')
    
    context = {
        'profiler': profiler,
        'post_count': Post.objects.filter(author=request.user).count(),
        'comment_count': Comment.objects.filter(author=request.user).count(),
    }
    return render(request, 'profiler/profiler_deletor.html', context)
