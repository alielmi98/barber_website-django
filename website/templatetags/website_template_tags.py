from django import template
from blog.models import Post,Category
from django.utils import timezone

register=template.Library()
@register.inclusion_tag("website/website_lastest_post.html")
def lastespost(arg=3):
    now=timezone.now()
    posts=Post.objects.filter(status=1).filter(published_date__lte = now).order_by('-published_date')[:arg]
    return {'posts':posts}