from django.contrib import admin
from .models import Client, Vendor, Category, Product, Sale, Sale_Product

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    pass 
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
@admin.register(Sale_Product)
class Sale_ProductAdmin(admin.ModelAdmin):
    pass