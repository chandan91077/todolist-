from django.db import models


class TodoList(models.Model):
    """Model to represent a to-do list"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Task(models.Model):
    """Model to represent a task in a to-do list"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.todo_list.title})"
