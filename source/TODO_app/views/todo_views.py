from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from TODO_app.forms import TodoForm
from TODO_app.models import TODO


def view_todos(request: WSGIRequest):
    todos = TODO.objects.exclude(is_deleted=True)
    return render(request, 'index.html', context={'todos': todos})


def create_todo(request: WSGIRequest):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'create_todo.html', context={'form': form})
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_todo', )
        else:
            return render(request, 'create_todo.html', context={'form': form})


def update_todo(request: WSGIRequest, pk):
    todo = get_object_or_404(TODO, pk=pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'update_todo.html', context={'form': form, 'todo': todo})
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('detail_todo', pk=todo.pk)
        else:
            return render(request, 'update_todo.html', context={'form': form})


def delete_todo(request: WSGIRequest, pk):
    todo = get_object_or_404(TODO, pk=pk)
    return render(request, 'todo_confirm_delete.html', context={'todo': todo})


def confirm_delete(pk):
    todo = get_object_or_404(TODO, pk=pk)
    todo.delete()
    return redirect('todos')


def detail_todo(request: WSGIRequest, pk):
    todo = get_object_or_404(TODO, pk=pk)
    return render(request, 'detail_todo.html', context={'todo': todo})
