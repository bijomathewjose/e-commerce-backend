from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=254,null=False)
    class Meta:
        db_table='customer'

class Product(models.Model):
    name=models.CharField(max_length=50,null=False)
    description=models.TextField(max_length=200)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=False)
    is_active=models.BooleanField(default=True)
    class Meta:
        db_table='product'

