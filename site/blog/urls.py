from django.conf.urls import url
import blog.views


urlpatterns = [
    url(r'^/?$', blog.views.index, name='index'),
    url(r'^(?P<slug>.+)/$', blog.views.post, name='post'),
    url(r'^author/(?P<author>.+)/$', blog.views.posts_by_author, name='posts_by_author'),
]
