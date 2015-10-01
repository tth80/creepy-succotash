from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
    return render(request, 'blog/index.html', {})


def post(request, slug):
    post_obj = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {'post': post_obj})
