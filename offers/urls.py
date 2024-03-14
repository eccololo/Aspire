from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="view-home"),
    path('offers', views.offers, name="view-offers"),
    path('about', views.about, name="view-about"),
    path('contact', views.contact, name="view-contact"),
]
