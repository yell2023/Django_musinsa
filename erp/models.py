from django.db import models
from accounts.models import UserModel
# from django.utils import timezone




class ProductModel(models.Model):
    class Meta:
        db_table = "product"
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_id = models.CharField(unique=True,max_length=20)
    product_name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1,default='Free')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_id

    def save(self, *args, **kwargs):
        return ''


class Inbound(models.Model):
    class Meta:
        db_table = "inbound"
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Outbound(models.Model):
    class Meta:
        db_table = "outbound"

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventory(models.Model):
    class Meta:
        db_table = "inventory"

    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE, related_name='inventory')
    stock_quantity = models.IntegerField(default=0)
