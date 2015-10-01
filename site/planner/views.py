from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Plan, Task, TaskSubtype, TaskStatus


def index(request):
    return render(request, 'planner/index.html', {})


@login_required
def api_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id, author=request.user)
    return JsonResponse(plan.to_json())


@login_required
def api_plan_list(request):
    ret = {'plans': [plan.to_json(summary=True)
        for plan in Plan.objects.filter(author=request.user).order_by('order')]}
    return JsonResponse(ret)
