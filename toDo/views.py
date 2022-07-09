from django.shortcuts import render
from rest_framework import viewsets
from .models import toDo
from .serializers import toDoSerializer
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

# Create your views here.

class toDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = toDo.objects.all().order_by('created_at')
    serializer_class = toDoSerializer
    permission_classes = [] # permissions.IsAuthenticated --> It requires you to be logged in to use the API.

    def create(self, request): # This function is always called by POST requests.
        newToDo = toDo.objects.create(title = request.POST.get('title', ''), 
                                      description = request.POST.get('description', ''), 
                                      user = request.user,)

        serialized_toDo = serializers.serialize('json', [newToDo, ]) 
        return HttpResponse(serialized_toDo, content_type ='application/json')

def displayBoard(request):
    if request.method == 'POST' and request.POST.get('toDoTitle') != '' and request.POST.get('toDoDescription') != '':
        title = request.POST.get('toDoTitle')
        description = request.POST.get('toDoDescription')
        newToDo = toDo.objects.create(title = title, description = description, user = request.user)
        newToDoSerialized = serializers.serialize('json', [ newToDo, ])
        return JsonResponse(newToDoSerialized[1:-1], safe = False)

    toDos = toDo.objects.all()

    return render(request, 'toDos-board.html', {'toDos': toDos})