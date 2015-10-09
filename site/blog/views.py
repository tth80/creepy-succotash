from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_sidebar = Post.objects.all().order_by('-created_at')[:5]

    return render(request, 'blog/index.html', {
        'posts': posts,
        'posts_sidebar': posts_sidebar})


def post(request, slug):
    post_obj = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {'post': post_obj})


def posts_by_author(request, author):
    pass
