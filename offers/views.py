from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib import messages

def home(request):
    return render(request, template_name="index.html")

@login_required(login_url="login")
def offers(request):
    return render(request, template_name="offers.html")

def about(request):
    return render(request, template_name="about.html")

@login_required(login_url="login")
def contact(request):
    return render(request, template_name="contact.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, template_name="dashboard.html")

def user_logout(request):
    auth.logout(request)
    # messages.success(request, "Logout success!") 
    return redirect("view-home")
