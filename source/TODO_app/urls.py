from django.urls import path

from TODO_app.views.todo_views import view_todos, create_todo

urlpatterns = [
    path('', view_todos, name='todos'),
    path('create/todo', create_todo, name='create_todo'),
]
