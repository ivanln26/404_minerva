from django.contrib import admin

from . import models


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = ('id', 'sale', 'product', 'quantity', 'unitary_price')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'dni', 'phone', 'email')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'stock', 'category')


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = ('id', 'state', 'vendor', 'client', 'location', 'create_at')


@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):

    pass
