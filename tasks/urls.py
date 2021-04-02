from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasklist, name='task-list'),
    path('task/<int:id>', views.taskview, name="task-view"),
    path('newtask/', views.newtask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourname, name='your-name'),
]
