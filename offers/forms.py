from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django_recaptcha.fields import ReCaptchaField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField()

    # username = UsernameField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': '',
    #         'id': 'hi',
    #     }
# ))