import uuid
from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,null=False)    
    description=models.TextField(max_length=300,null=False)

class Product(models.Model):
    name=models.CharField(max_length=50,null=False)
    description=models.TextField(max_length=300)
    price=models.IntegerField(null=False)
    image=models.URLField(validators=[URLValidator()])
    category=models.ManyToManyField(Category)
    stock=models.IntegerField(default=0)
    active=models.BooleanField()
    register_date=models.DateTimeField(auto_now=True,null=False)
    
