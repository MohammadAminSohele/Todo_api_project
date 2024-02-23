from rest_framework import serializers

from .models import Task_model

class Task_serializer(serializers.ModelSerializer):
    class Meta:
        model=Task_model
        fields='__all__'