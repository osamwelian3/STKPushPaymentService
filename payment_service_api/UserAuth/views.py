from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login, get_user_model, logout
from payment_service_api.settings import AUTH_USER_MODEL
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class=RegisterSerializer

    def get_queryset(self):
        pass

    def list(self, request):
        if request.user.is_staff:
            return Response({'Users': list(User.objects.all().values('username', 'email', 'is_active', 'is_staff', 'last_login'))})
        return Response({'User': request.user.username})

    @action(methods=['GET'], detail=False, url_path='/')
    def auth_state(self, request):
        if request.user.is_authenticated:
            return Response({'success': 'Authenticated as '+request.user.username})
        else:
            return Response({'failed': 'Not authenticated'})

    @action(methods=['POST'], detail=False)
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False, serializer_class=LoginSerializer)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "Login successful"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({'success': 'logout success'})
