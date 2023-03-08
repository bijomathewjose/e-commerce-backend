from django.urls import path
from .views import CustomerProductList,AddCustomers,ListCustomers,AddProducts,ListProducts,AddCategories,ListCategories,ListProductCategories,BuyProducts

urlpatterns = [
    path('customer/<int:customer_id>/products',CustomerProductList.as_view(),name='customerproducts'),
    path('customer/add',AddCustomers.as_view(),name='add_customer'),
    path('customers',ListCustomers.as_view(),name='list_customers'),
    path('product/add',AddProducts.as_view(),name='add_product'),
    path('products/',ListProducts.as_view(),name='list_products'),
    path('product/<int:product_id>/categories',ListProductCategories.as_view(),name='categoryproducts'),
    path('category/add',AddCategories.as_view(),name='add_category'),
    path('categories/',ListCategories.as_view(),name='list_categories'),
    path('buy-product/', BuyProducts.as_view(), name='buy-product'),
]
