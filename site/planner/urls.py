from django.conf.urls import url
import planner.views

urlpatterns = [
    url(r'^$', planner.views.index),
]
