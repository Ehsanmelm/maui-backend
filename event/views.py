from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EventModel, EventUserModel
from .serializers import CreateEventSerializer , EventUserSerializer , EventDetailSerializer

# Create your views here.

class CreateEventUserView(APIView):
        
    def get(self , request , id ):
        queryset = EventModel.objects.filter(event_maker= id)
        serializer = CreateEventSerializer(queryset , many=True)
        
        return Response(serializer.data)
    
    def post(self , request , id ):
        serializer = CreateEventSerializer(data= request.data  , context = {'request' : request , 'id':id})
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    
    # def put(self,request , id ):
    #     queryset = EventModel.objects.get(id = event_id)
    #     serializer = CreateEventSerializer(data= request.data  , context = {'request' : request , 'id':id})
    #     serializer.is_valid(raise_exception = True)
    #     serializer.save()

    #     return Response(serializer.data)

class EvetnUserView(APIView):
    def get(self, request, id):
        queryset = EventUserModel.objects.filter(event_picker = id)
        serializer = EventUserSerializer(queryset , many =True)

        return Response(serializer.data)
        
    def post(self,request, id):
        serializer = EventUserSerializer(data= request.data  , context = {'request' : request , 'id':id})
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    
class ShowEventsView(APIView):
    def get(self,request):
        queryset = EventModel.objects.all()
        seriailzer = CreateEventSerializer(queryset , many= True)

        return Response(seriailzer.data)
    
class EventDetailView(APIView):
    def get(self,request, id):
        queryset = EventModel.objects.get(id=id)
        serializer = EventDetailSerializer(queryset)

        return Response(serializer.data)