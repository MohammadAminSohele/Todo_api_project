from rest_framework import serializers

from .models import Todo_model

class Todo_serializer(serializers.ModelSerializer):
    class Meta:
        model=Todo_model
        fields='__all__'