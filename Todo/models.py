from django.db import models

# Create your models here.

class Todo_model(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    priority=models.IntegerField()
    is_done=models.BooleanField(default=False)

    def __str__(self):
        return self.title