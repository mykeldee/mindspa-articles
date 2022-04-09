from django.urls import path
from . import views

urlpatterns = [
    path('',views.ArticleCreateListView.as_view(), name='articles'),
    path('<int:id>/',views.ArticleDetailView.as_view(), name='article_detail'),
]