from rest_framework import generics,response,status
from customer.models import CustomerShoppingList,Customer
from product.models import Category,Product
from .serializers import ShoppingListSerializer,CustomerSerializer,ProductSerializer,CategorySerializer,ProductCategorySerializer

class CustomerProductList(generics.ListAPIView):
    serializer_class=ShoppingListSerializer

    def get_queryset(self):
        customer_id=self.kwargs['customer_id']
        return CustomerShoppingList.objects.filter(customer_id=customer_id)
    
class AddCustomers(generics.CreateAPIView):
    serializer_class=CustomerSerializer
    queryset=Customer.objects.all()
    
class ListCustomers(generics.ListAPIView):
    serializer_class=CustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.all()
    
class AddProducts(generics.CreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
class ListProducts(generics.ListAPIView):
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all()

class ListCategories(generics.ListAPIView):
    serializer_class=CategorySerializer
    def get_queryset(self):
        return Category.objects.all()
    
class AddCategories(generics.CreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class ListProductCategories(generics.ListAPIView):
    serializer_class=ProductCategorySerializer

    def get_queryset(self):
        product_id=self.kwargs['product_id']
        return Product.objects.get(id=product_id).category.all()

class BuyProducts(generics.CreateAPIView,generics.ListAPIView):
    serializer_class=ShoppingListSerializer

    def get_queryset(self):
        customer_id=self.kwargs['customer_id']
        return CustomerShoppingList.objects.filter(customer_id=customer_id)
    
    def create(self, request, *args, **kwargs):
        customer = customer_id=self.kwargs['customer_id']
        customer_product_list=CustomerShoppingList.objects.filter(customer_id=customer_id)
        product_list=Product.objects.all()
        
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
 