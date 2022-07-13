from rest_framework import viewsets
from .models import toDo
from .serializers import toDoSerializer
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

class toDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows toDos to be viewed or edited.
    """
    queryset = toDo.objects.all().order_by('created_at')
    serializer_class = toDoSerializer
    permission_classes = [] # permissions.IsAuthenticated --> It requires you to be logged in to use the API.

    """
    Creates a new toDo in the API when a POST request is made.
    """
    def create(self, request): # This function is always called by POST requests.
        newToDo = toDo.objects.create(title = request.POST.get('title', ''), 
                                      description = request.POST.get('description', ''))

        serialized_toDo = serializers.serialize('json', [newToDo, ]) 
        return HttpResponse(serialized_toDo, content_type ='application/json')

"""
Displays the board with all toDos* and, if a POST request is made, creates a new toDo in the local database**. It also returns 
the new toDo in json format so that it can be displayed on the board.
"""
def displayBoard(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    
    if request.method == 'POST' and title != '' and description != '':   
        newToDo = toDo.objects.create(title = title, description = description)
        newToDoSerialized = serializers.serialize('json', [ newToDo, ])
        return JsonResponse(newToDoSerialized[1:-1], safe = False)

    toDos = toDo.objects.all()

    return render(request, 'toDos-board.html', {'toDos': toDos}) 

"""
* All locally created toDos.

** IMPORTANT UPDATE! --> I made some changes. The toDo is no longer created in the local database. ONLY IN THE API.

IMPORTANT! --> The main difference between the functions create and displayBoard is that the first one is the one that actually
creates the toDo in the API. The second one, apart from displaying the board, creates the toDo locally. That means, if you only had
the displayBoard function and opened the application on a local server, you'd only be able to create toDos in the local database.
You wouldn't be creating anything in the API.
"""                