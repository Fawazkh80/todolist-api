from django.db import models

class Box(models.Model):
    name =models.CharField(max_length=50)
class Task(models.Model):
    title = models.TextField(max_length = 50)
    desc = models.TextField(max_length = 150)
    box = models.ForeignKey(Box, related_name="tasks", on_delete=models.CASCADE) 
