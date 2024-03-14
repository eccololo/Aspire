from django.shortcuts import render

def home(request):
    return render(request, template_name="index.html")

def offers(request):
    return render(request, template_name="offers.html")
