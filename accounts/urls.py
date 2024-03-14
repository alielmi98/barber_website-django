from django.contrib import admin
from django.urls import path
from .views import login_view,logout_view,signup_view
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls.base import reverse_lazy
app_name='accounts'

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('signup/',signup_view,name='signup'),

]