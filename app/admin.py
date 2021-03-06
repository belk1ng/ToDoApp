from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'is_complete', 'published_at']
    list_display_links = ['id', 'task']
    ordering = ['-id']


admin.site.register(Task, TaskAdmin)
# dmitry dmitry
