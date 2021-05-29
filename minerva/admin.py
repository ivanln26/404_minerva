from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Sale_Product)
class Sale_ProductAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):

    pass
