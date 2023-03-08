from django.db import models
from product.models import Product

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)

    class Meta:
        db_table='customers'
        
    def __str__(self):
        return self.name
    
class CustomerShoppingList(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

    class Meta:
        db_table='customer_shopping_list'
