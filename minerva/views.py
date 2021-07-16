from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View

from . import models
from .forms import LoginForm, ProductForm


def index(request):
    products = models.Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'index.html', ctx)


class ProductCreateView(View):

    def get(self, request):
        return render(request, 'product_create.html')

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido correctamente.', 'alert-success')
        else:
            messages.error(request, 'No se pudo añadir el producto.', 'alert-danger')
        return redirect('product_list')


class ProductDeleteView(View):

    def get(self, request, id):
        try:
            product = models.Product.objects.get(pk=id)
            product.delete()
            messages.info(request, 'Producto eliminado correctamente.', 'alert-dark')
        except ObjectDoesNotExist:
            messages.error(request, 'No se pudo eliminar el producto.', 'alert-danger')
        finally:
            return redirect('product_list')


class ProductDetailView(View):

    def get(self, request, id):
        try:
            product = models.Product.objects.get(pk=id)
            ctx = {
                'product': product,
            }
            return render(request, 'product_detail.html', ctx)
        except ObjectDoesNotExist:
            messages.error(request, 'No se pudo encontrar el producto.', 'alert-danger')
            return redirect('product_list')


class ProductEditView(View):

    def get(self, request, id):
        try:
            product = models.Product.objects.get(pk=id)
            ctx = {
                'product': product,
            }
            return render(request, 'product_edit.html', ctx)
        except ObjectDoesNotExist:
            messages.error(request, 'No se pudo encontrar el producto.', 'alert-danger')
            return redirect('product_list')

    def post(self, request, id):
        try:
            product = models.Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
            if not form.is_valid():
                # TODO(any): show form errors.
                messages.error(request, 'Error en formulario.', 'alert-danger')
                return redirect('product_edit', id=id)
            form.save()
            messages.success(request, 'Producto editado correctamente.', 'alert-success')
            return redirect('product_list')
        except ObjectDoesNotExist:
            messages.error(request, 'No se pudo encontrar el producto.', 'alert-danger')
            return redirect('product_list')


class ProductListView(View):

    def get(self, request):
        ctx = {
            'products': models.Product.objects.all(),
        }
        return render(request, 'product_list.html', ctx)


class LoginView(LoginView):

    template_name = 'login.html'
    authentication_form = LoginForm
