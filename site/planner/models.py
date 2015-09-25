from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='plans')

    def __str__(self):
        return 'Plan #{}: {}'.format(self.id, self.title)


class Task(models.Model):
    plan = models.ForeignKey(Plan, related_name='tasks')
    title = models.CharField(max_length=100)

    def __str__(self):
        return 'Task #{}.{}: {}'.format(self.plan_id, self.id, self.title)
