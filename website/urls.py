from django.contrib import admin
from django.urls import path
from .views import index_view,about_view,services_view,pricing_view,contact_view,appointment_view,newsletter_view
app_name='website'
urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('services',services_view,name='services'),
    path('pricing',pricing_view,name='pricing'),
    path('contact',contact_view,name='contact'),
    path('appointment',appointment_view,name='appointment'),
    path('newsletter',newsletter_view,name='newsletter'),

]