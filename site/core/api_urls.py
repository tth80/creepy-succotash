from django.conf.urls import url
import core.views


urlpatterns = [
    url(r'^user/$', core.views.api_user_info),
]
