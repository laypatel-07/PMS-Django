from django.contrib import admin
from .models import Project, Task


admin.site.site_title = 'Project management system'
admin.site.site_header = 'Project Management System - Admin Dashboard'
admin.site.index_title = 'Index Administration'

# Custom admin for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'projectname', 'create_at', 'updated_at')
    search_fields = ('projectname',)
    list_filter = ('create_at', 'updated_at')
    ordering = ('-create_at',)

# Custom admin for Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'assigned_to', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'project__projectname', 'assigned_to__username')
    list_filter = ('status', 'priority', 'assigned_to', 'due_date')
    ordering = ('-created_at',)

# Register models with custom admins
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
