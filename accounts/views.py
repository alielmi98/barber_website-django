from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import SignupForm
import sweetify


    

def login_view(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    sweetify.success(request, "Login successful!")
                    return redirect('/')
            else:
                sweetify.error(request, "Username or Password is invalid, please try again!")
                

                    
        
        form=AuthenticationForm()
        contex={'form':form}
        return render(request,"accounts/login.html",contex)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  
            sweetify.success(request, 'You have signed up successfully!')  
        else:
            sweetify.error(request, 'Sign up failed, please try again!')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})