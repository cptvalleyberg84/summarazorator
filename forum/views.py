from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    # template_name = "post_list.html"
    template_name = 'forum/index.html'
    paginate_by = 6

def post_detail(request, slug):
    """
    Display individual :model:'forum.Post'.
    Template :template:'forum/post_detail.html'
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        'forum/post_detail.html',
        {'post': post},
    )
