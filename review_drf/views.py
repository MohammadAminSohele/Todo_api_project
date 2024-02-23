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