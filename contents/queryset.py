from .models import Post,Tag,Reaction
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Count, Q
from users.models import User

# fial
def get_post_with_more_likes():
    posts_with_likes = Post.objects.annotate(like_count=Count('reaction', filter=Q(reaction__status='1')))
    posts_ordered_by_likes = posts_with_likes.order_by('-like_count')
    post_with_most_likes = posts_ordered_by_likes.first()
    return post_with_most_likes
    


def get_today_posts_like_counts(user):
    today = timezone.now().date()
    today_posts = Post.objects.filter(owner__username=user, created_at__date=today)
    total_likes = Reaction.objects.filter(post__in=today_posts, status='1').count()
    return total_likes


def get_tag_with_more_post():
    tag_with_more_post = Tag.objects.annotate(post_count=Count('post')).order_by('-post_count').first()
    return tag_with_more_post


def sum_of_post_in_30_days(user):
    thirty_days_ago = datetime.now() - timedelta(days=30)
    post_count = Post.objects.filter(owner__username=user, created_at__gte=thirty_days_ago).count()
    return post_count


# get_post_with_more_likes()