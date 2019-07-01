from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Event,Comment
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .forms import CommentForm
# Create your views here.



def index(request):
    context = {}
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'event/index.html', context=context)

# Event Details Page with comments 
def event(request,item_id):
    # context = {'index':item_id}

    #events all objects
    event = Event.objects.get(pk=item_id)
    pk_event_heading = str(event)
    print('events-',pk_event_heading)

    #comment all objects
    comments = Comment.objects.all()
    event_comments = Comment.objects.filter(event=item_id)
    total_comments = len(event_comments)
    print(total_comments)
    # print(event_comments)
    # print('item id -',item_id)
    # for s in event_comments:
    #   print('user-',s.author,'event-',s.event,'text-',s.text)

    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'event/event_details.html', {'index':item_id,'event_comments':event_comments,'total_comments':total_comments,})

#add comment view
""" def add_comment_to_post(request,pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = event
            comment.save()

            return redirect('event',pk=event.pk)
        
        else:
            form = CommentForm()
        return render(request,'event/add_comment_to_post.html')

 """

#test api token
class HelloView(APIView):

    #check api authentication
    # permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'msg':'Hellow,from API'}
        return Response(content)


'''Api list view '''
class EventList(generics.ListCreateAPIView):

    #check api authentication
    # permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetails(generics.RetrieveUpdateDestroyAPIView):

    #check api authentication
    # permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

#Requesting token
# http post http://127.0.0.1:8000/api-token-auth/ username=rashedoz password=sakura342

#Api call httpie
#http http://127.0.0.1:8000/event/ 'Authorization: Token c85c0db20a11fdc080ee9379d684e6165384d0d9'

#Api call curl
#curl http://127.0.0.1:8000/event/4/ -H 'Authorization: Token c85c0db20a11fdc080ee9379d684e6165384d0d9'

#Delete api element
#curl -X DELETE http://127.0.0.1:8000/event/4/ -H 'Authorization: Token c85c0db20a11fdc080ee9379d684e6165384d0d9'
