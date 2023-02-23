from django.urls import path

from TODO_app.views.todo_views import view_todos, create_todo, detail_todo, update_todo, delete_todo, confirm_delete

urlpatterns = [
    path('', view_todos, name='todos'),
    path('create/todo', create_todo, name='create_todo'),
    path('detail/todo/<int:pk>', detail_todo, name='detail_todo'),
    path('update/todo/<int:pk>', update_todo, name='update_todo'),
    path('delete/todo/<int:pk>', delete_todo, name='delete_todo'),
    path('confirm/delete/todo/<int:pk>', confirm_delete, name='confirm_delete'),
]
