from django.urls import path,include
from rest_framework import routers

from . views import CategoryViewset,ProductViewSet,CustomerViewSet,AddCustomerProducts

router=routers.DefaultRouter()
router.register(r'categories',CategoryViewset)
router.register(r'products',ProductViewSet)
router.register(r'customers',CustomerViewSet)
router.register(r'customer/add/Product',AddCustomerProducts)
urlpatterns = [
    path('',include(router.urls)),
]
