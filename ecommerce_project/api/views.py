from rest_framework import viewsets,views,status,response
from products.models import Products
from categories.models import Categories
from customers.models import Customers,CustomerProducts
from . serializers import CategorySerializers,ProductSerializers,CustomerSerializer,ProductListSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Categories.objects.all()
    serializer_class=CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customers.objects.all()
    serializer_class=CustomerSerializer

class AddCustomerProducts(viewsets.ModelViewSet):
    queryset=CustomerProducts.objects.all()
    serializer_class=ProductListSerializer
