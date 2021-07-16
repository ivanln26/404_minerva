from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View

from . import models
from .forms import ClientForm, LoginForm, ProductForm


def index(request):
    products = models.Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'index.html', ctx)


class ClientCreateView(View):

    def get(self, request):
        return render(request, 'client_create.html')

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente añadido correctamente.', 'alert-success')
        else:
            messages.error(request, 'No se pudo añadir un nuevo cliente.', 'alert-danger')
        return redirect('client_list')


class ClientEditView(View):

    def get(self, request, id):
        try:
            client = models.Client.objects.get(pk=id)
            ctx = {
                'client': client,
            }
            return render(request, 'client_edit.html', ctx)
        except ObjectDoesNotExist:
            messages.error(request, 'No se pudo encontrar el cliente.', 'alert-danger')
            return redirect('client_list')

    def post(self, request, id):
        try:
            client = models.Client.objects.get(pk=id)
            form = ClientForm(request.POST, instance=client)
            if not form.is_valid():
                # TODO(any): show form errors.
                messages.error(request, 'Error en formulario.', 'alert-danger')
                return redirect('client_edit', id=id)
            form.save()
            messages.success(request, 'Cliente editado correctamente.', 'alert-success')
            return redirect('client_list')
        except ObjectDoesNotExist:
            messages.error(request, 'No se pudo encontrar el cliente.', 'alert-danger')
            return redirect('client_list')


class ClientListView(View):

    def get(self, request):
        ctx = {
            'clients': models.Client.objects.all(),
        }
        return render(request, 'client_list.html', ctx)


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
