from django.contrib import admin

from .models import Task, TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "todo_list", "created_at")
    list_filter = ("todo_list",)
    search_fields = ("title",)
    ordering = ("-created_at",)
