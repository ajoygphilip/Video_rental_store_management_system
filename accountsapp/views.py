from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Profile
from .serailziers import ProfileSerializer, UserRegistrationSerializer

class MemberViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@api_view(['POST',])
def registration_view(request):
    data={}
    
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        
        token = Token.objects.get_or_create(user=account)[0].key

        data["response"] = "Registration Succesful"
        data["token"] = token
        return Response(data)
    else:
        return Response(serializer.errors)
    

@api_view(['POST',])
def logout_view(request):
    
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)
    
    