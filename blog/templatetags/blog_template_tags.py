from django import template
from blog.models import Post,Category,Comment
from django.utils import timezone

register=template.Library()

@register.inclusion_tag("blog/blog_lastes_post.html")
def lastespost(arg=3):
    now=timezone.now()
    posts=Post.objects.filter(status=1).filter(published_date__lte = now).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag("blog/blog_categoris.html")
def postcategories():
    now=timezone.now()
    posts=Post.objects.filter(status=1).filter(published_date__lte = now)
    categories=Category.objects.all()
    cat_dic={}
    for name in categories:
        count=posts.filter(category=name).count()
        if count>0:
            cat_dic[name]=count
    return {'categories':cat_dic}

@register.simple_tag(name="comments_count")
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()