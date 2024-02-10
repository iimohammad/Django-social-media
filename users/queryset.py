from django.db.models import Avg
from users.models import User
from contents.models import Comment,Post

def get_user_with_more_average_comments():
    user_comments_avg = User.objects.annotate(
        average_comments=Avg('posts__comment__id')
    ).order_by('-average_comments').first()
    return user_comments_avg


def following_count(user):
    userobj = User.objects.get(username = user)
    return userobj.followings.count()

def follow_user(user1, user2):
    user1obj = User.objects.get(username = user1)
    user2obj = User.objects.get(username = user2)
    user1obj.followings.add(user2obj)
    
        
