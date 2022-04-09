from django.contrib import admin
from .models import Article

# Register your models here.    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','title','description','content','author','created_at','category']
    list_filter=['created_at','category','author']