from django.contrib import admin
from django.urls import path
from .views import blog_index_view,blog_single_view,blog_search_view
app_name='blog'
urlpatterns = [
    path('',blog_index_view,name='index'),
    path('<int:pid>',blog_single_view,name='single'),
    path('category/<str:cat_name>',blog_index_view,name='category'),
    path('tags/<str:tag_name>',blog_index_view,name='tags'),
    path('author/<str:author_name>',blog_index_view,name='author'),
    path('search/',blog_search_view,name='search'),
]