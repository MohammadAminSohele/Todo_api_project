from django.urls import path

from .import views

urlpatterns = [
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<int:pk>/', views.taskDetail, name="task-Detail"),
    path('task-create/', views.taskCreate, name="task-Create"),
     path('task-update/<int:pk>/', views.taskUpdate, name="task-update"),
]
