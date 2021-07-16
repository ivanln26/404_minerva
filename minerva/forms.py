from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import Product


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'