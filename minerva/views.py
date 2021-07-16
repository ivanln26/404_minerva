from django.contrib.auth import views as auth_views
from django.shortcuts import render

from . import models
from .forms import LoginForm


def index(request):
    products = models.Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'index.html', ctx)


class LoginView(auth_views.LoginView):

    template_name = 'login.html'
    authentication_form = LoginForm
