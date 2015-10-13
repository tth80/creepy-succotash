from django.conf.urls import url
import planner.views

urlpatterns = [
    url(r'^api/plan/(?P<plan_id>[1-9][0-9]*)/$', planner.views.api_plan, name="plan"),
    url(r'^api/plans/$', planner.views.api_plan_list, name="plans"),

    url(r'^new/$', planner.views.PlanCreate.as_view(), name="new"),
    url(r'^edit/(?P<pk>[0-9]+)/$', planner.views.PlanUpdate.as_view(), name="edit"),
    
    url(r'^(?P<slug>[-_\w]+)/$', planner.views.plan, name="plan"),
    url(r'^(?P<plan>[-_\w]+)/(?P<task>[-_\w]+)/$', planner.views.task, name="task"),
    url(r'^(?P<slug>[-_\w]+)/new/(?P<type>[-_\w]+)/$', planner.views.TaskCreate.as_view(), name="task_create"),

    url(r'^$', planner.views.index, name="index"),
]
"""
reserved keywords: new/edit/delete

/plans/
/plans/new/ <-- restrict keywords
/plans/carpachio-modeo/
/plans/carpachio-modeo/new/idea/ <-- restrict keywords
/plans/carpachio-modeo/edit/
/plans/carpachio-modeo/delete/
/plans/carpachio-modeo/user-interface/
/plans/carpachio-modeo/user-interface/edit/
/plans/carpachio-modeo/user-interface/delete/

"""
