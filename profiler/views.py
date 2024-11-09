from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forum.models import Post, Comment
from .models import Profiler
from .forms import ProfilerForm


@login_required  # Ensures only logged-in users can access this view
def profiler_page(request):
    """
    Renders the Profiler page
    """
    user = request.user

    try:
        profiler = Profiler.objects.get(user=user)
    except Profiler.DoesNotExist:
        # Optionally create a new Profiler instance for the user or handle missing profile
        profiler = Profiler.objects.create(user=user)

    # Set latest posts and comments
    profiler.last_posts.set(Post.objects.filter(author=user).order_by('-created_on')[:3])
    profiler.last_comments.set(Comment.objects.filter(author=user).order_by('-created_on')[:3])
    profiler.save()

    # Initialize or handle form submission
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


def profiler_edit(request, profiler_id):
    """
    View to edit the profiler
    """
    profiler = get_object_or_404(Profiler, id=profiler_id, user=request.user)

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
            'profiler_form': profiler_form
        },
    )