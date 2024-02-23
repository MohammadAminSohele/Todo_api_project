from django.db import models

# Create your models here.

class Task_model(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    priority=models.IntegerField()
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    description=models.TextField()

    def __str__(self):
        return self.title