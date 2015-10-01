from django.contrib import admin
from .models import Plan, Task, TaskSubtype, TaskStatus


class TaskAdmin(admin.ModelAdmin):
    model = Task


class TaskStatusInline(admin.TabularInline):
    model = TaskStatus
    extra = 0


class TaskSubtypeAdmin(admin.ModelAdmin):
    model = TaskSubtype
    inlines = [TaskStatusInline]


admin.site.register(Plan)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskSubtype, TaskSubtypeAdmin)
admin.site.register(TaskStatus)
