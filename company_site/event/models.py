from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    event_heading = models.CharField(max_length=50)
    event_details = models.CharField(max_length=500)
    event_date = models.DateField('event date')
    
    #upload to media folder in gallery (media/gallery)
    event_banner = models.ImageField(upload_to='gallery/',default=None)

    #return onject explaination
    def __str__(self):
        return self.event_heading

    #check event date 
    def is_event_over(self):
        return self.event_date >= timezone.now() - datetime.timedelta(days=1)