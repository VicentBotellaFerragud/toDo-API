from rest_framework import serializers
from .models import toDo

class toDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = toDo
        fields = ['id','title', 'description', 'created_at'] # 'user' could be added as well.