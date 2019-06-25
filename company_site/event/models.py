from django.db import models
import datetime
from django.utils import timezone

from stdimage.models import StdImageField
# Create your models here.

class Event(models.Model):
    event_heading = models.CharField(max_length=20)
    event_details = models.CharField(max_length=500)
    event_date = models.DateField('event date')
    
    #upload to media folder in gallery (media/gallery)
    event_banner = StdImageField(upload_to='gallery/new', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200,True),
        'home' : (690, 398),
    })

   

    #return onject explaination
    def __str__(self):
        return self.event_heading

    #check event date 
    def is_event_over(self):
        return self.event_date >= timezone.now() - datetime.timedelta(days=1)