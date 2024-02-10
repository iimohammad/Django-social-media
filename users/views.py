from django.db.models import Count, Avg
from django.http import HttpResponse
from .queryset import following_count,follow_user,get_user_with_more_average_comments
from .models import User

def user_with_more_average_comments_view(request):
    return HttpResponse(get_user_with_more_average_comments())


def follow_user_view(request, username1, username2):
    try:
        user2 = User.objects.get(username=username2)
        if username2 == username1:
            return HttpResponse("Failed")
        else:
            follow_user(username1, username2)
            return HttpResponse(user2.display_name())
    except User.DoesNotExist:
        return HttpResponse("Failed")


def count_following_view(request, user):
    return HttpResponse(following_count(user=user))
