from multiprocessing import context
from django.db import models

class ToDoItem(models.Model):
    content = models.TextField(max_length=150)