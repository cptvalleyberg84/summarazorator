from django.shortcuts import render, get_object_or_404
from .models import Profiler
from forum.models import Post, Comment, User


def profiler_page(request):
    """
    Renders the Profiler page
    """
    # profiler = Profiler.objects.all().order_by('-updated_on').first()
    # user = get_object_or_404(User, username=username)

    user = request.user  # Get the currently logged-in user
    profiler = get_object_or_404(Profiler, user=user)  # Get or create the user's profile
    
    profiler.last_posts.set(Post.objects.filter(author=user).order_by('-created_on')[:3])
    profiler.last_comments.set(Comment.objects.filter(author=user).order_by('-created_on')[:3])

    profiler.save()


    return render(
        request,
        "profiler/profiler.html",
        {"profiler": profiler},
    )