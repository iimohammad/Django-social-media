from django.http import HttpResponse
from .queryset import get_post_with_more_likes,get_tag_with_more_post,get_today_posts_like_counts,sum_of_post_in_30_days


def post_with_more_likes_view(request):
    return HttpResponse(get_post_with_more_likes())


def today_posts_like_counts_view(request, username):
    return HttpResponse(get_today_posts_like_counts(username))


def tag_with_more_posts_view(request):
    return HttpResponse(get_tag_with_more_post())


def sum_of_posts_in_last_30_days_view(request, username):
    return HttpResponse(sum_of_post_in_30_days(username))
