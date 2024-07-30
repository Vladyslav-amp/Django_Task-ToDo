from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, ImageUploadForm
from .utils import analyze_task, handle_uploaded_image

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            importance, category, description = analyze_task(task.title)
            task.importance = importance
            task.category = category
            task.description = description
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save()
            importance, category, description = analyze_task(task.title)
            task.importance = importance
            task.category = category
            task.description = description
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/update.html', {'form': form, 'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/delete.html', {'task': task})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.files['image']
            result = handle_uploaded_image(image)
            return render(request, 'todo/result.html', {'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'todo/upload.html', {'form': form})