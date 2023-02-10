from django.shortcuts import render
from django import http
from django.views import View
from .models import Payment
from .serializers import PaymentSerializer, PhoneSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class=PaymentSerializer
    queryset=Payment.objects.all()

    @action(detail=False, methods=['post'], serializer_class=PhoneSerializer)
    def pay(self, request, *args, **kwargs):
        if request.method == 'POST':
            phone = request.POST.get('phone_number') if request.POST.get('phone_number') is not None else request.data.get('phone_number')
            return Response({'post_success': phone})
        return Response({'error': 'failed'})
        # user = self.get_object()
        # serializer = PasswordSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.validated_data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)

