from django.shortcuts import render
from rest_framework import viewsets
from .models import toDo
from .serializers import toDoSerializer

# Create your views here.

class toDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = toDo.objects.all().order_by('created_at')
    serializer_class = toDoSerializer
    permission_classes = [] # permissions.IsAuthenticated --> It requires you to be logged in to use the API.