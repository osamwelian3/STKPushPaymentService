from django.shortcuts import render
from django import http
from django.views import View
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import viewsets

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class=PaymentSerializer
    queryset=Payment.objects.all()

class Pay(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            phone = request.POST.get('phone')
        return JsonResponse({'MSSID', phone})

    def dispatch(self, request: http.HttpRequest, *args, **kwargs) -> http.HttpResponse:
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
