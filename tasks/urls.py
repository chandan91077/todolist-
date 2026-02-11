from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-task/', views.create_task, name='create_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]
