from rest_framework import serializers
from product.models import Product,Category,ProductCategories
from customer.models import Customer,CustomerShoppingList

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=ProductCategories
        fields=('category','category_id')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class ShoppingListSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=CustomerShoppingList
        fields=('product','quantity')



