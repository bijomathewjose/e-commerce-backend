from rest_framework import serializers

from products.models import Products
from categories.models import Categories
from customers.models import Customers,CustomerProducts

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=('id','name','description')

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        categories=CategorySerializers(many=True,read_only=True)
        model=Products
        fields=('id', 'name', 'description', 'price', 'image_url','stock','categories')
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('first_name','last_name','email_id','password','mobile_num')

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProducts
        fields=('id','product_id','customer_id','quantity')  
