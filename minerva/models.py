from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Vendor(AbstractUser):

    phone = models.CharField(max_length=20, blank=True)


class Client(models.Model):

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dni = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Category(models.Model):

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):

    name = models.CharField(max_length=25)
    price = models.FloatField(validators=[MinValueValidator(0)])
    stock = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Sale(models.Model):

    PREORDER = "PO"
    PENDING = 'PD'
    FINALIZED = 'FI'
    STATE_CHOICES =[(PREORDER, 'Pre-Venta'),(PENDING, 'En proceso'),(FINALIZED, 'Concretado')]
    OFFICE = "OF"
    MERCADOLIBRE = "ML"
    WEBSITE = "WS"
    INSTAGRAM = "IG"
    LOCATION_CHOICES = [(OFFICE, 'Oficina'), (MERCADOLIBRE, 'Mercado Libre'),(WEBSITE, 'Pagina Web'), (INSTAGRAM, 'Instagram')]
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=PENDING)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=2,choices=LOCATION_CHOICES, default=MERCADOLIBRE)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.state}'


class CartItem(models.Model):

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField()
    unitary_price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.id}: {self.product} - {self.quantity}'
