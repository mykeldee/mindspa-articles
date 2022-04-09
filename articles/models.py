from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()

class Article(models.Model):
    CATEGORY=(
        ('MEDITATION','meditation'),
        ('NUTRITION','nutrition'),
        ('EXERCISE','exercise')
    )
    title=models.CharField(max_length=50,blank=True,null=True)
    description=models.CharField(max_length=50, blank=True, null=True)
    content=models.CharField(max_length=5000)
    #author=models.ForeignKey(User, on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    category=models.CharField(max_length=20,choices=CATEGORY,default=CATEGORY[0][0])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"<Article {self.title} by {self.author.id}>"
    