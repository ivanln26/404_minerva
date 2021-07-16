from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View

from . import models
from .forms import LoginForm


def index(request):
    products = models.Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'index.html', ctx)


class ProductListView(View):

    def get(self, request):
        ctx = {
            'products': models.Product.objects.all(),
        }
        return render(request, 'product_list.html', ctx)


class LoginView(LoginView):

    template_name = 'login.html'
    authentication_form = LoginForm
