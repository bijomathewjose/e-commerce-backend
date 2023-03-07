import uuid
from django.db import models
from django.core.validators import URLValidator
from datetime import date
from django.utils import timezone

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50,null=False)    
    description=models.TextField(max_length=300,null=False)

class Product(models.Model):
    name=models.CharField(max_length=50,null=False)
    description=models.TextField(max_length=300)
    price=models.IntegerField(null=False)
    image=models.URLField(validators=[URLValidator()])
    product_categories=models.ManyToManyField(Categories)
    stock=models.IntegerField(default=0)
    active=models.BooleanField()
    register_date=models.DateField(default=date.today,null=False)

    def validate_registration(self):
        two_months_ago = timezone.now() - timezone.timedelta(days=60)
        if self.registration_date > two_months_ago:
            self.active = False

    def save(self, *args, **kwargs):
        self.validate_registration()
        super().save(*args, **kwargs)    

    class Meta:
        db_table='products'