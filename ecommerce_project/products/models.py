from django.db import models
from django.core.validators import URLValidator
from categories.models import Categories
from datetime import timedelta,date

class Products(models.Model):
    
    name=models.CharField(max_length=50,null=False,unique=True)
    description=models.TextField(max_length=300)
    price=models.FloatField(null=False)
    image_url=models.URLField(max_length=2000,null=False,validators=[URLValidator()])
    stock=models.IntegerField(default=0,null=False)
    categories=models.ManyToManyField(Categories)
    is_active=models.BooleanField(default=True,null=False)
    registration_date=models.DateTimeField(auto_now_add=True,null=False)

    def is_registration_active(self):
        time_limit=date.today()-timedelta(days=60)
        if self.registration_date>time_limit:
            self.is_active=False
    
    def save(self,*args,**kwargs):
            self.is_registration_active() 
            super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='products'