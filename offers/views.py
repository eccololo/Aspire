from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, template_name="index.html")

def offers(request):
    return render(request, template_name="offers.html")

def about(request):
    return render(request, template_name="about.html")

def contact(request):
    return render(request, template_name="contact.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, template_name="dashboard.html")
