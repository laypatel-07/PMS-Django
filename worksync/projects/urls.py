from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("tasks/", views.task_menu, name="task_menu"),
    path("home/", views.home, name="home"),
    # Keep existing URLs
    path("", views.project_list, name="project_list"),
    path("create/", views.project_create, name="project_create"),
    path("<int:project_id>/edit/", views.project_edit, name="project_edit"),
    path("<int:project_id>/delete/", views.project_delete, name="project_delete"),
    path("register/", views.register, name="register"),
    path("<int:project_id>/tasks/", views.task_list, name="task_list"),
    path("<int:project_id>/tasks/create/", views.task_create, name="task_create"),
    path("<int:project_id>/tasks/<int:task_id>/edit/", views.task_edit, name="task_edit"),
    path("<int:project_id>/tasks/<int:task_id>/delete/", views.task_delete, name="task_delete"),
]