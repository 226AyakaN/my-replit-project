from django.db import models

# Create your models here.
# todo/models.py
from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# todo/models.py

from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)  # ← これを追加
