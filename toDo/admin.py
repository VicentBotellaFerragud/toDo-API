from django.contrib import admin
from .models import toDo

class toDoAdmin(admin.ModelAdmin):    
    fields = ('title', 'description', 'created_at', 'user',)    
    list_display = ('title', 'description', 'created_at', 'user',)    
    search_fields = ('title',)

# Register your models here.

admin.site.register(toDo, toDoAdmin)
