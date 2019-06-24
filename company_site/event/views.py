from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def index(request):
    return HttpResponse('Event Page')

#test api token
class HelloView(APIView):

    #check api authentication
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'msg':'Hellow,from API'}
        return Response(content)


'''Api list view '''
class EventList(generics.ListCreateAPIView):

    #check api authentication
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetails(generics.RetrieveUpdateDestroyAPIView):

    #check api authentication
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

#Requesting token
# http post http://127.0.0.1:8000/api-token-auth/ username=rashedoz password=sakura342

#Api call httpie
#http http://127.0.0.1:8000/event/ 'Authorization: Token c85c0db20a11fdc080ee9379d684e6165384d0d9'

#Api call curl
#curl http://127.0.0.1:8000/hello/ -H 'Authorization: Token c85c0db20a11fdc080ee9379d684e6165384d0d9'
