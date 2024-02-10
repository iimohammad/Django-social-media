from django.urls import path

from .views import *
urlpatterns = [
    path('users/1',user_with_more_average_comments_view),
    path('users/2',follow_user_view),
    path('users/3',count_following_view),
]