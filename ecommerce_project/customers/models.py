from django.db import models
from products.models import Products
from django.core.validators import EmailValidator

class Customers(models.Model):
    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(unique=True, max_length=254,null=False,validators=[EmailValidator()])
    password = models.CharField(max_length=128,null=False)
    mobile_num = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True,null=False)


    class Meta:
        db_table='customers'

    def __str__(self):
        return self.first_name
    
    

class CustomerProducts(models.Model):
    customer_id=models.ForeignKey(Customers,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False)
    created_date=models.DateTimeField(auto_now_add=True,null=False)
    
    class Meta:
        db_table='customer_products'

    
