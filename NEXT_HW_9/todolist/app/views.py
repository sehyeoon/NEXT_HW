from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone

def home(request):
    tasks = Task.objects.order_by('deadline')
    today = timezone.now()  # 현재 날짜와 시간을 가져오기 (시간대를 고려하여)
    for task in tasks:
        task.days_until_deadline = (task.deadline - today).days  # 남은 일수 계산해서 새로운 변수에 저장
    return render(request, 'home.html', {'tasks': tasks, 'today': today})

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'detail.html', {'task': task})

def new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'new.html', {'form': form})

def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TaskForm(instance=task)
    return render(request, 'update.html', {'form': form, 'task': task})

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'detail.html', {'task': task})
