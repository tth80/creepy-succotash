from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


PLAN_STATUS_CHOICES = (
    ('PE', _('Pending')),
    ('PL', _('Planning')),
)

RESTRICTED_KEYWORDS = ('edit', 'new', 'delete', 'api')


class Plan(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='plans')
    status = models.CharField(max_length=2, choices=PLAN_STATUS_CHOICES,
                              default='PE')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Plan #{}: {}'.format(self.id, self.title)

    def to_json(self, summary=False):
        if summary:
            return {
                'id': self.id,
                'title': self.title,
                'status': self.get_status_display(),
                'order': self.order,
                }

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.get_status_display(),
            'created_at': self.created_at,
            'modified_at': self.created_at,
            'order': self.order,
            'tasks': [task.to_json() for task in self.tasks.all()],
            }

    def get_max_order(user_id):
        try:
            max_order = Plan.objects.filter(author_id=user_id) \
                .values('order').order_by('-order')[0]['order']
        except:
            max_order = -1
        return max_order

    class Meta:
        unique_together = (('author', 'slug'),)


class Task(models.Model):
    plan = models.ForeignKey(Plan, related_name='tasks')
    slug = models.SlugField(max_length=50)

    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    subtype = models.ForeignKey('TaskSubtype', related_name='tasks+')
    order = models.PositiveIntegerField(default=0)
    status = models.ForeignKey('TaskStatus', related_name='tasks2+')
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Task #{}.{}: {}'.format(self.plan_id, self.id, self.title)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'type': self.subtype.name,
            'order': self.order,
            'status': self.status.name,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            }
    
    def get_max_order(user_id):
        try:
            max_order = Task.objects.filter(plan__author_id=user_id) \
                .values('order').order_by('-order')[0]['order']
        except:
            max_order = -1
        return max_order

    class Meta:
        unique_together = (('plan', 'slug'),)


class TaskSubtype(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Task Subtype: #{}: {}'.format(self.id, self.name)


class TaskStatus(models.Model):
    name = models.CharField(max_length=50)
    subtype = models.ForeignKey('TaskSubtype', related_name='statuses+')
    default_new = models.BooleanField(default=False)

    def __str__(self):
        return 'Task Status: #{}: {} ({})'.format(self.id, self.name, self.subtype.name)
