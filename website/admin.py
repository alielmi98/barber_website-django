from django.contrib import admin
from .models import Contact,NewsLetter,Appointment

# Register your models here.

@admin.register(Contact)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsLetter)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AuthorAdmin(admin.ModelAdmin):
    pass