from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,null=True,blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering=['created_date']
    def __str__(self):
        return self.name



class NewsLetter(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email


class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{10,11}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 12)
    date = models.DateField(null=False,blank=False)
    time=models.TimeField(null=False,blank=False)
    service=models.CharField(max_length=255)
    barber=models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering=['date', 'time']
    def __str__(self):
        return self.name
