from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-task/', views.create_task, name='create_task'),
    path('edit-task/<slug:slug>/', views.edit_task, name='edit_task'),
    path('delete-task/<slug:slug>/', views.delete_task, name='delete_task'),
    path('task/<slug:slug>/', views.task_detail, name='task_detail'),
    # path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('task/<int:task_id>/', views.task_detail, name='task_detail'),
]
