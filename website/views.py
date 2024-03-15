from django.shortcuts import render,redirect
from .models import Contact,NewsLetter
from .forms import ContactForm,NewsLetterForm,AppointmentForm
from django.contrib import messages
import sweetify


def index_view(request):
    return render(request,"website/index.html")

def about_view(request):
    return render(request,"website/about.html")

def services_view(request):
    return render(request,"website/services.html")

def pricing_view(request):
    return render(request,"website/pricing.html")

def contact_view(request):
    form=ContactForm(request.POST)
    
    if request.method=="POST":
        if form.is_valid():
            form.save()
            sweetify.success(request, "Your ticket has been sent.")
        else:
            sweetify.error(request, "Your message was not sent")

    return render(request,"website/contact.html",{'form': form})

def appointment_view(request):
    if  request.user.is_authenticated:
        form=AppointmentForm(request.POST)
    
        if request.method=="POST":
            if form.is_valid():
                form.save()
                sweetify.success(request, "Your Appointment request has been registered")
            else:
                sweetify.error(request, "Your request was not sent")
        return render(request,"website/appointment.html",{'form': form})
    else:
        sweetify.info(request, "please login or signup first")
        return redirect('/accounts/login/')


def newsletter_view(request):
    form=NewsLetterForm(request.POST)
    if form.is_valid():
        form.save()
        sweetify.success(request, "Your email has been successfully registered.")
    else:
        sweetify.error(request, "Your email was not registered. Please try again")
        
    return redirect(request.META['HTTP_REFERER'])
