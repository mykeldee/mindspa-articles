#from django_mongoengine import QuerySet
from . models import Article
from rest_framework import serializers


class ArticleCreationSerializer(serializers.ModelSerializer):
    title=serializers.CharField()
    author=serializers.CharField()
    description=serializers.CharField()
    content=serializers.CharField(max_length=50000)
    category=serializers.HiddenField(default='MEDITATION')
    
    
    class Meta:
        model=Article
        fields=['title','author','description','content', 'category']
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField()
    author=serializers.CharField()
    description=serializers.CharField()
    content=serializers.CharField(max_length=50000)
    category=serializers.CharField(default='MEDITATION')
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    
    
    class Meta:
        model=Article
        fields=['title','author','description','content', 'category','created_at','updated_at']