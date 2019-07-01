from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from stdimage.models import StdImageField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Event(models.Model):
    event_heading = models.CharField(max_length=20)
    event_details = models.CharField(max_length=500)
    event_date = models.DateField('event date')
    event_score = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    
    #upload to media folder in gallery (media/gallery)
    event_banner = StdImageField(upload_to='gallery/new', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200,True),
        'home' : (690, 398),
    })

   

    #return object explaination
    def __str__(self):
        return self.event_heading

    #check event date 
    def is_event_over(self):
        return self.event_date >= timezone.now() - datetime.timedelta(days=1)

#Comment Model

class Comment(models.Model):
    event = models.ForeignKey('event.Event',on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name="creator")
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    comment_score = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(10)])

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
