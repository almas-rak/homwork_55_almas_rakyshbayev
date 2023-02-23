from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

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
            return redirect('todos')
        else:
            return render(request, 'create_todo.html', context={'form': form})


