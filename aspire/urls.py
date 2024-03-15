from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("offers.urls")),
    path("", include("contacts.urls")),
    path('login', auth_views.LoginView.as_view(), name="login")
]
