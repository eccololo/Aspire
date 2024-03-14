from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="view-home"),
    path('offers', views.offers, name="view-offers"),
]
