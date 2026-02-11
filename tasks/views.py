from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Task
from .forms import TaskForm


# Show all tasks
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


# Create new task view post
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/create_task.html', {'form': form})


# Delete task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    
    return render(request, 'tasks/delete_task.html', {'task': task})
