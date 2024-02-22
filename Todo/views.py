from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Todo_model
from .serializer import Todo_serializer

# Create your views here.

@api_view(['GET','POST'])
def all_todos(request:Request):
    if request.method=='GET':
        Todo_query=Todo_model.objects.order_by('priority').all()
        Todo_query_serialize=Todo_serializer(instance=Todo_query,many=True)
        return Response(data=Todo_query_serialize.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        Todo_deserialize=Todo_serializer(data=request.data)
        if Todo_deserialize.is_valid():
            Todo_deserialize.save()
            return Response(data=Todo_deserialize.data,status=status.HTTP_201_CREATED)
    return Response(data=None,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def todo_detail(request:Request,todo_id):
    try:
        todo_query=Todo_model.objects.get(pk=todo_id)
    except Todo_model.DoesNotExist:
        return Response(None,status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        todo_serialize=Todo_serializer(instance=todo_query)
        return Response(data=todo_serialize.data,status=status.HTTP_202_ACCEPTED)
    elif request.method=='PUT':
        todo_edit=Todo_serializer(instance=todo_query,data=request.data)
        if todo_edit.is_valid():
            todo_edit.save()
            return Response(data=todo_edit.data,status=status.HTTP_202_ACCEPTED)
        return Response(None,status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        todo_query.delete()
        return Response(data=None,status=status.HTTP_204_NO_CONTENT)