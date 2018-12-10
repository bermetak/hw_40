from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    return render(request, 'index.html', context={
        'tasks': Task.objects.all()
    })


def create_task_view(request):
    task = Task.objects.create(
        name=request.POST.get('task_name')
    )
    return redirect('task_index')


def delete_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('task_index')

def done_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_done.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('done') == 'yes':
            task.status = 'done'
            task.save()
        return redirect('task_index')


def edit_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_edit.html', context={
            'task': task
        })
    elif request.method == 'POST':
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()

        return redirect('task_index')

def in_progress_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_in_progress.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('in_progress') == 'yes':
            task.status = 'in_progress'
            task.save()
        return redirect('task_index')

def delete_done_tasks(request):
    task = Task.objects.filter(status='done')
    if request.method == 'GET':
        return render(request, 'done_task_delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('task_index')