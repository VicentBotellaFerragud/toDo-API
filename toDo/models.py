from django.db import models
import datetime
from django.conf import settings

# Create your models here.

class toDo(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 30)
    created_at = models.DateField(default = datetime.date.today)
    # User is optional.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = None, blank = True, null = True)

    def time_since_its_creation(self):
        currentDay = datetime.date.today()
        passedTime = currentDay - self.created_at
        return str(passedTime.days) + ' ' + 'days.'