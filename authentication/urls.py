from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserListView.as_view(), name='user_list'),
    path('signup/',views.UserCreateView.as_view(), name='sign_up'),
    path('login/',views.UserCreateView.as_view(), name='sign_up'),
]