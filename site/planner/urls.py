from django.conf.urls import url
import planner.views

urlpatterns = [
    url(r'^$', planner.views.index, name="index"),
    url(r'^api/plan/(?P<plan_id>[1-9][0-9]*)/$', planner.views.api_plan, name="plan"),
    url(r'^api/plans/$', planner.views.api_plan_list, name="plans"),
]
