from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """Display list of all posts on the index page."""
    queryset = Post.objects.all()
    template_name = 'forum/index.html'
    paginate_by = 6


def post_detail(request, post_slug):
    """
    Display individual post and handle comment submission.

    Args:
        request: The HTTP request
        post_slug: The slug of the post to display
    """
    queryset = Post.objects.filter(post_status=1)
    post = get_object_or_404(queryset, post_slug=post_slug)
    comments = post.comments.order_by('-comment_created_on')

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.parent_post = post
            comment.comment_author = request.user
            comment.comment_type = request.POST.get('comment_type', 'positive')
            comment.save()
            messages.success(request, 'Comment submitted.')
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()

    return render(
        request,
        'forum/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        },
    )


def comment_edit(request, post_slug, comment_id):
    """
    Handle editing of existing comments.

    Args:
        request: The HTTP request
        post_slug: The slug of the parent post
        comment_id: The ID of the comment to edit
    """
    if request.method == "POST":
        queryset = Post.objects.filter(post_status=1)
        post = get_object_or_404(queryset, post_slug=post_slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.comment_author == request.user:
            comment = comment_form.save(commit=False)
            comment.parent_post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[post_slug]))


def comment_delete(request, post_slug, comment_id):
    """
    Handle deletion of existing comments.

    Args:
        request: The HTTP request
        post_slug: The slug of the parent post
        comment_id: The ID of the comment to delete
    """
    queryset = Post.objects.filter(post_status=1)
    post = get_object_or_404(queryset, post_slug=post_slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.comment_author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[post_slug]))


@login_required
def create_post(request):
    """Handle creation of new posts."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.post_slug = slugify(post.post_title)
            post.save()
            return redirect('post_detail', post_slug=post.post_slug)
    else:
        form = PostForm()

    return render(request, 'forum/create_post.html', {
        'form': form,
        'title': 'Create Post'
    })


def search_posts(request):
    """
    Search for posts based on title or content.

    Args:
        request: The HTTP request containing the search query
    """
    query = request.GET.get('searchbar')
    if query:
        posts = Post.objects.filter(
            Q(post_title__icontains=query) |
            Q(post_content__icontains=query)
        ).distinct()
    else:
        posts = []

    return render(request, 'forum/search_results.html', {
        'posts': posts,
        'query': query
    })


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)
