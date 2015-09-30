from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Post


def frontpage(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_sidebar = Post.objects.all().order_by('-created_at')[:5]

    return render(request, 'frontpage.html', {
        'posts': posts,
        'posts_sidebar': posts_sidebar})

@login_required
def api_user_info(request):
    user = request.user
    data = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }

    return JsonResponse(data)
