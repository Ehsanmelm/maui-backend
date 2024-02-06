from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel 
from .serializers import UserRegisterSerializer , LoginUserSerializer

# Create your views here.

class RegisterUserView(APIView):
    def post(self , request):
        serializer = UserRegisterSerializer(data= request.data )
        serializer.is_valid(raise_exception = True)
        if UserModel.objects.filter(email = serializer.validated_data['email']).exists():
            return Response(" there is a same account with this email")
        
        else:
            serializer.save()
            return Response(serializer.data)

        # return Response(serializer.data)

class LoginUserView(APIView):
    def post(self,request):
        serializer = LoginUserSerializer(data= request.data )
        serializer.is_valid(raise_exception=True)

        try:

            loged_user= UserModel.objects.get( email = serializer.validated_data['email'] ,password = serializer.validated_data['password'])
            
            context = {}
            context['id'] = loged_user.id
            context['email'] = loged_user.email

            return Response(context)
        except UserModel.DoesNotExist:
            return Response(0)
