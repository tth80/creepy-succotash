from django.conf.urls import url
import redtab.views


urlpatterns = [
    url(r'^$', redtab.views.index),
]

