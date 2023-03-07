import uuid
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
# Create your models here.

class User(models.Model):
    user_id=models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
    first_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30)
    email_id=models.EmailField(unique=True, max_length=254,null=False,validators=[EmailValidator()])
    password=models.CharField(max_length=128,null=False)
    mobile_num=models.IntegerField(null=False)
    admin=models.BooleanField(default=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True,null=False)

    def set_password(self,password):
        self.password=make_password(password)

    class Meta:
        db_table='user'