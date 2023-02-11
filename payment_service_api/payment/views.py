from django.shortcuts import render
from django import http
from django.views import View
from .models import Payment
from .serializers import PaymentSerializer, PhoneSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .transaction_handler import Transaction
import json

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class=PaymentSerializer
    queryset=Payment.objects.all()

    @action(detail=False, methods=['post'], serializer_class=PhoneSerializer)
    def pay(self, request, *args, **kwargs):
        if request.method == 'POST':
            phone = request.POST.get('phone_number') if request.POST.get('phone_number') is not None else request.data.get('phone_number')
            transaction = Transaction()
            tr = transaction.stk_push(phone=phone, amount=1)
            if 'errorMessage' in tr:
                return Response({'error': tr['errorMessage']},status=400)
            if 'ResponseCode' in tr:
                if tr['ResponseCode'] == '0':
                    validation = transaction.query_transaction(tr['CheckoutRequestID'])
                    print(validation)
                    while 'errorMessage' in validation:
                        validate = transaction.query_transaction(tr['CheckoutRequestID'])
                        if 'ResultDesc' in validate:
                            if validate['ResultDesc'] == "The initiator information is invalid.":
                                message = "Something went wrong"
                                return Response({'error': message}, status=400)
                            if validate['ResultDesc'] == "DS timeout user cannot be reached":
                                message = "Your phone cannot be reached to initiate transaction"
                                return Response({'error': message}, status=400)
                            if validate['ResultDesc'] == "Request cancelled by user":
                                message = "You took too long or cancelled the PIN request for the transaction Please try again"
                                return Response({'error': message}, status=400)
                            if validate['ResultDesc'] == "The service request is processed successfully.":
                                message = "Yey... Payment went through"
                                return Response({'success': message})
                            
            return Response({'error': 'Something went wrong'})
        return Response({'error': 'Something went wrong'})

    @action(detail=False, methods=['post', 'get'])
    def callback(self, request, *args, **kwargs):
        if request.method == 'POST':
            transaction_id = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[1].get('Value')
            phone_number = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[3].get('Value')
            amount = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[0].get('Value')
            status = request.data.get('Body').get('stkCallback').get('ResultDesc')
            payment = Payment.objects.create(transaction_id, phone_number, amount, status, payment)
            payment.save()
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return Response(dict(context))

