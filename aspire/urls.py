from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from offers.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", include("offers.urls")),
    path("", include("contacts.urls")),
    path('login', auth_views.LoginView.as_view(template_name="registration/login.html",
            authentication_form=UserLoginForm), name="login")
]
