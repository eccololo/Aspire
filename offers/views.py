from django.shortcuts import render

def home(request):
    return render(request, template_name="index.html")

def offers(request):
    return render(request, template_name="offers.html")

def about(request):
    return render(request, template_name="about.html")

def contact(request):
    return render(request, template_name="contact.html")
