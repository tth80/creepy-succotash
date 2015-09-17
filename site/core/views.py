from django.shortcuts import render
from blog.models import Post


def frontpage(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_sidebar = Post.objects.all().order_by('-created_at')[:5]

    return render(request, 'frontpage.html', {
        'posts': posts,
        'posts_sidebar': posts_sidebar})
