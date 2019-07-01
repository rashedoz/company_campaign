from django.forms import ModelForm
from .models import Event,Comment

'''Comment Form'''
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)



    

