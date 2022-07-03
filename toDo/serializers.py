from rest_framework import serializers
from .models import toDo
from django.contrib.auth.models import User

# I have to define this class first so that the toDoSerializer() class can make use of it.
class userSerializer(serializers.HyperlinkedModelSerializer): 
    
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name']

class toDoSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault()) --> Option provided by Django framework.
    user = userSerializer()
    
    class Meta:
        model = toDo
        fields = ['id','title', 'description', 'created_at', 'user', 'time_since_its_creation']