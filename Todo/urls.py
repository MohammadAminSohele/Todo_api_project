from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .import views

router=DefaultRouter()
router.register('',views.TodoViewsetApiView)

urlpatterns = [
    path('all',views.all_todos),
    path('all/<int:todo_id>',views.todo_detail),
    path('all/cbv',views.todos_ApiView.as_view()),
    path('all/mixin',views.Todos_mixin.as_view()),
    path('all/mixin/<pk>',views.Todo_mixin.as_view()),
    path('all/generics',views.Todos_generics.as_view()),
    path('all/generics/<pk>',views.Todo_generics.as_view()),
    path('viewsets/',include(router.urls)),
]