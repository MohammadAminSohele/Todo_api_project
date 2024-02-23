from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task_model
from .serializer import Task_serializer


# Create your views here.
@api_view(['GET'])
def taskList(request:Request):
    tasks_query=Task_model.objects.order_by('priority').all()
    tasks_serializer=Task_serializer(instance=tasks_query,many=True)
    return Response(data=tasks_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def taskDetail(request:Request,pk):
    task_query=Task_model.objects.get(id=pk)
    task_serializer=Task_serializer(instance=task_query)
    return Response(data=task_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def taskCreate(request:Request):
    if request.method=='GET':
        tasks_query=Task_model.objects.order_by('priority').all()
        tasks_serializer=Task_serializer(instance=tasks_query,many=True)
        return Response(data=tasks_serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        task_deserializer=Task_serializer(data=request.data)
        if task_deserializer.is_valid():
            task_deserializer.save()
            return Response(data=task_deserializer.data,status=status.HTTP_201_CREATED)
        return Response(data=None,status=status.HTTP_400_BAD_REQUEST)