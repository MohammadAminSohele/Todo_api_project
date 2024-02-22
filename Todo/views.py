from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics

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

class todos_ApiView(APIView):
    def get(self,request:Request):
        all_todos_query=Todo_model.objects.order_by('priority').all()
        instance_all_todos_query=Todo_serializer(instance=all_todos_query,many=True)
        return Response(instance_all_todos_query.data,status=status.HTTP_200_OK)
    def post(self,request:Request):
        data_todo=Todo_serializer(data=request.data)
        if data_todo.is_valid():
            data_todo.save()
            return Response(data=data_todo.data,status=status.HTTP_201_CREATED)
        
class Todos_mixin(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Todo_model.objects.order_by('priority').all()
    serializer_class=Todo_serializer    

    def get(self,request:Request):
        return self.list(request)
    
    def post(self,request:Request):
        return self.create(request)
    

class Todo_mixin(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Todo_model.objects.order_by('priority').all()
    serializer_class=Todo_serializer

    def get(self,request:Request,pk):
        return self.retrieve(request)
    def put(self,request:Request,pk):
        return self.update(request)
    def delete(self,request:Request,pk):
        return self.destroy(request)
        

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