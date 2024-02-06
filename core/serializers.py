from rest_framework import serializers , status
from rest_framework.response import Response
from .models import UserModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    # def che

class LoginUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = UserModel
        fields = ['id' , 'email' , 'password']

    # def create(self,request):
    #     try:
    #         loged_user = user.objects.get(id = self.context["request"].id , name = self.context['request'].name ,password = self.context['request'].password )
    #         # return Response(loged_user)
    #         return Response(status=status.HTTP_200_OK)
        
    #     except user.DoesNotExist:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

            
