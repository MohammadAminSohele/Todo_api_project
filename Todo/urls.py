from django.urls import path

from .import views

urlpatterns = [
    path('all',views.all_todos),
    path('all/<int:todo_id>',views.todo_detail),
]