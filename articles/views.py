from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg2.utils import swagger_auto_schema
from . import serializers
from .models import Article
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
# class HelloArticleView(generics.GenericAPIView):
#     def get(self,request):
#         return Response(data={"message":"Hello Article"}, status = status.HTTP_200_OK)


class ArticleCreateListView(generics.GenericAPIView):
    serializer_class= serializers.ArticleCreationSerializer
    queryset=Article.objects.all()
    #permission_classes=[IsAuthenticatedOrReadOnly]
    
    @swagger_auto_schema(operation_summary="Retrieve all articles")
    def get(self,request):
        articles = Article.objects.all()
        serializer=self.serializer_class(instance=articles, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Add an article")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        #user=request.user

        if serializer.is_valid():
            serializer.save()
           # serializer.save(author=user)
           
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(generics.GenericAPIView):
    serializer_class=serializers.ArticleDetailSerializer
    permission_classes=[IsAdminUser]
    
    @swagger_auto_schema(operation_summary="View article details")
    def get(self,request,id):
        article=get_object_or_404(Article,pk=id)
        serializer=self.serializer_class(instance=article)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Edit and article")
    def put(self,request):
        data=request.data
        article=get_object_or_404(Article,pk=id)
        serializer=self.serializer_class(data=data, instance=article)
    
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete an article")
    def delete(self,request):
        article=get_object_or_404(Article,pk=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    