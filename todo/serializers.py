from . import models
from rest_framework import serializers

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
      model  = models.Box
      fields  =   "__all__"
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
      model  = models.Task
      fields  =   "__all__"