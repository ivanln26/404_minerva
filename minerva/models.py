from django.contrib.auth.models import AbstractUser
from django.db import models


class Vendor(AbstractUser):

    phone = models.CharField(max_length=20, blank=True)


class Client(models.Model):

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dni = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class Category(models.Model):

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):

    name = models.CharField(max_length=25)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Sale(models.Model):

    state = models.CharField(max_length=20)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=20)
    create_at = models.DateField(auto_now_add=True)


class Sale_Product(models.Model):

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    unitary_price = models.FloatField()
