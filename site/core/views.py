from django.shortcuts import render
from blog.models import Post

def frontpage(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'frontpage.html', {'posts': posts})
