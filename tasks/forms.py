from django import forms
from .models import TodoList, Task


class TodoListForm(forms.ModelForm):
    """Form for creating TodoList"""
    
    class Meta:
        model = TodoList
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter list title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter list description (optional)',
            }),
        }


class TaskForm(forms.ModelForm):
    """Form for creating Task"""
    
    todo_list = forms.ModelChoiceField(
        queryset=TodoList.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="----------"
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'todo_list']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter task description (optional)',
            }),
        }
