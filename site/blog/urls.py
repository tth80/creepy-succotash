from django.conf.urls import url
import blog.views


urlpatterns = [
    url(r'^(?P<slug>.+)/$', blog.views.post),
]
