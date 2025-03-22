from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, ProductView

router = DefaultRouter()
router.register(r'categories', CategoryView)
router.register(r'product', ProductView)
 

urlpatterns = [
    path('', include(router.urls))
]  