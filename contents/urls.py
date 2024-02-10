from django.urls import path
from .views import *
urlpatterns = [
    path('contents/1',post_with_more_likes_view),
    path('contents/2',today_posts_like_counts_view),
    path('contents/3',tag_with_more_posts_view),
    path('contents/4',sum_of_posts_in_last_30_days_view)
]
