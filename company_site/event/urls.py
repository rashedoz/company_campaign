from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [

    path('',views.index,name='index'),
    path('event_details/<int:item_id>/',views.event,name='event'),

    path('event/',views.EventList.as_view()),
    path('event/<int:pk>/',views.EventDetails.as_view()),

    path('hello/',views.HelloView.as_view(),name ='hello'),

    #request api tokens
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

]

urlpatterns = format_suffix_patterns(urlpatterns)