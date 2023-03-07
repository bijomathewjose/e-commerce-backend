from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50,null=False,unique=True)
    description=models.TextField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='categories'