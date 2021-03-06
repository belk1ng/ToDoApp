from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-pk')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data)
            return redirect('home')

    return render(request, 'app/index.html', {'tasks': tasks, 'form': form})


def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'app/update_task.html', {'task': task, 'form': form})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'app/delete_task.html', {'task': task})
