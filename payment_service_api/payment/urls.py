from .views import PaymentViewSet, Pay
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register('payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pay/', Pay.as_view(), name='make_payment')
]