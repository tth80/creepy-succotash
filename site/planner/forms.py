from datetime import datetime

from django.core.urlresolvers import reverse_lazy, reverse
from django.forms import ModelForm, TextInput
from django.forms.models import modelform_factory
from django.views.generic.edit import CreateView, UpdateView
from django.utils.text import slugify

from .models import Plan, Task, TaskSubtype, TaskStatus, RESTRICTED_KEYWORDS  # , TaskSubtype, TaskStatus

class TaskCreate(CreateView):
    model = Task
    form_class = modelform_factory(Task,
            widgets={'title': TextInput(attrs={'placeholder': 'xxx', 'autofocus': 'autofocus'})},
        fields=('title', 'body', 'status',))

    def get_form(self, form_class=None):
        form = super(TaskCreate, self).get_form(form_class)
        form.fields['status'].queryset = TaskStatus.objects.filter(subtype__slug=self.kwargs.get('type', ''))
        form.fields['status'].initial = form.fields['status'].queryset.filter(default_new=True).first()
        return form

    def form_valid(self, form):
        max_order = Task.get_max_order(self.request.user.id)

        try:
            plan = Plan.objects.get(slug=self.kwargs.get('slug', ''),
                                    author_id=self.request.user.id)
        except Plan.DoesNotExist:
            return False

        try:
            subtype = TaskSubtype.objects.get(slug=self.kwargs.get('type', ''))
        except TaskSubtype.DoesNotExist:
            return False

        form.instance.slug = slugify(form.instance.title)
        form.instance.plan = plan
        form.instance.subtype = subtype
        form.instance.author = self.request.user
        form.instance.order = max_order + 1
        form.instance.created_at = datetime.now()

        if form.instance.slug in RESTRICTED_KEYWORDS:
            return False

        return super(TaskCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('planner:plan', kwargs={'plan': self.kwarg.get('plan')})

    """
    plan = models.ForeignKey(Plan, related_name='tasks')
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    subtype = models.ForeignKey('TaskSubtype', related_name='tasks+')
    order = models.PositiveIntegerField(default=0)
    status = models.ForeignKey('TaskStatus', related_name='tasks2+')
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    """


class PlanCreate(CreateView):
    model = Plan
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('planner:index')

    def form_valid(self, form):
        max_order = Plan.get_max_order(self.request.user.id)

        form.instance.slug = slugify(form.instance.title)
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
