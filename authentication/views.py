from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg2.utils import swagger_auto_schema
from .models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class=serializers.UserCreationSerializer
    
    @swagger_auto_schema(operation_summary="Create a user account")
    def post(self,request):
        data=request.data
        
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status = status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.GenericAPIView):
    serializer_class= serializers.UserListSerializer
    queryset=User.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    @swagger_auto_schema(operation_summary="View all user accounts")
    def get(self,request):
        users = User.objects.all()
        serializer=self.serializer_class(instance=users, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)