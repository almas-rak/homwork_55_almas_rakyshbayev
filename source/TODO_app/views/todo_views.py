from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from TODO_app.models import TODO


def view_todos(request: WSGIRequest):
    todos = TODO.objects.exclude(is_deleted=True)
    return render(request, 'index.html', context={'todos': todos})


