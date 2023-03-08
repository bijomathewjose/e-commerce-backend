from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    stock=models.DecimalField( max_digits=25,decimal_places=2)

    class Meta:
        db_table='products'

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='category'

    def __str__(self):
        return self.name
    
class ProductCategories(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='categories_product'
    
