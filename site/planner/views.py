from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import datetime
from .models import Plan, Task, TaskSubtype, TaskStatus
from .forms import PlanForm

class PlanCreate(CreateView):
    model = Plan
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('planner:index')

    def form_valid(self, form):
        max_order = Plan.get_max_order(self.request.user.id)

        form.instance.author = self.request.user
        form.instance.order = max_order + 1 
        form.instance.created_at = datetime.now()
        return super(PlanCreate, self).form_valid(form)


class PlanUpdate(UpdateView):
    model = Plan
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('planner:index')

    def form_valid(self, form):
        form.instance.modified_at = datetime.now()
        return super(PlanCreate, self).form_valid(form)


def index(request):
    plan = Plan.objects.get(id=1)
    plans = Plan.objects.filter(author_id=request.user.id)

    return render(request, 'planner/index.html', {'plan': plan, 'plans': plans})


@login_required
def api_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id, author=request.user)
    return JsonResponse(plan.to_json())


@login_required
def api_plan_list(request):
    ret = {'plans': [plan.to_json(summary=True)
        for plan in Plan.objects.filter(author=request.user).order_by('order')]}
    return JsonResponse(ret)
