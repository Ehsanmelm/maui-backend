from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user 
from .serializers import UserRegisterSerializer , LoginUserSerializer

# Create your views here.

class RegisterUserView(APIView):
    def post(self , request):
        serializer = UserRegisterSerializer(data= request.data )
        serializer.is_valid(raise_exception = True)
        if user.objects.filter(email = serializer.validated_data['email']).exists():
            return Response(" there is a same account with this email")
        
        else:
            serializer.save()
            return Response(serializer.data)

        # return Response(serializer.data)

class LoginUserView(APIView):
    def post(self,request):
        serializer = LoginUserSerializer(data= request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["name"]
        if user.objects.filter( name = serializer.validated_data['name'] ,password = serializer.validated_data['password']).exists():
            # user_date = UserRegisterSerializer()
            return Response(serializer.data)
        else:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(0)