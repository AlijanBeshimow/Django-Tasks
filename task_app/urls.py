from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView
from . import views

urlpatterns = [
    path('api/tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.task_list, name='task_list'),
    path('create/task/', views.create_task,
         name='create_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    path('search/', views.search_view, name='search'),
]
