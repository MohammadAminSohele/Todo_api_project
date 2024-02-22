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