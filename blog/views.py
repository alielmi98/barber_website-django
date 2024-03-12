from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.contrib import messages




def blog_index_view(request,**kvargs):
    now = timezone.now()
    posts=Post.objects.filter(published_date__lte = now).filter(status=True)

    if kvargs.get('cat_name') != None:
        posts=posts.filter(category__name=kvargs['cat_name'])
    
    if kvargs.get('author_name') != None:
        posts=posts.filter(author__username=kvargs['author_name'])

    if kvargs.get('tag_name') != None:
        posts=posts.filter(tags__name__in=[kvargs['tag_name']])


    posts = Paginator(posts, 3)
    try:
        page_number=request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
       posts = posts.get_page(1)
    except EmptyPage:
             posts = posts.get_page(1)


    
    
    contex={'posts':posts}
    return render(request,"blog/blog-home.html",contex)


def blog_single_view(request,pid):
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Comment has been sent.")
        else:
            messages.add_message(request, messages.ERROR, "Your Comment was not sent")
        return HttpResponseRedirect('/')

    form=CommentForm()
    now = timezone.now()
    post=get_object_or_404(Post,pk=pid,status=True,published_date__lte = now)
    post.counted_views+=1
    post.save()
    posts=Post.objects.filter(published_date__lte = now).filter(status=True)
    list_of_post=[]
    for i in posts:
        list_of_post.append(i.id)

    current_post_index=list_of_post.index(pid)
    next_post="This is a last post"
    prev_post="This is a first post"

    if(len(list_of_post)>(current_post_index+1)):
        next_post=Post.objects.get(pk=list_of_post[current_post_index+1])

    if(current_post_index !=0):
        prev_post=Post.objects.get(pk=list_of_post[current_post_index-1])
        
    comment=Comment.objects.filter(post=post.id,approved=True)
    contex={'post':post, 'next_post':next_post, 'prev_post':prev_post,'comment':comment,'form': form}
    return render(request,"blog/blog-single.html",contex)

def blog_search_view(request):
    now = timezone.now()
    posts=Post.objects.filter(published_date__lte = now).filter(status=True)
    if request.method=='GET':
        if s:= request.GET.get('s'):
            posts=posts.filter(content__contains=s)
        contex={'posts':posts}
    return render(request,"blog/blog-home.html",contex)