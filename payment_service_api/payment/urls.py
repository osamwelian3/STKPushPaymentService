from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register('payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]