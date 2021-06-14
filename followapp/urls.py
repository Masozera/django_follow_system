from django.urls import path
from .views import (
     user_list,
    SignUpView,
    user_detail,)
from followapp import views

app_name = 'followapp'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),

    path('users/follow/', views.user_follow, name='user_follow'),
]