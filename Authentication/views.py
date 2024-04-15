# Create your views here.


# Create your views here.

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from Authentication.models import CustomUser
from Authentication.serializers import UserSerializer, TokenObtainPairSerializer

def index(request):
	return render(request,'index.html')

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(generics.CreateAPIView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

class TokenRefreshView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
def post(self, request, *args, **kwargs):
    serializer = TokenObtainPairSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    refresh_token = serializer.validated_data.get('refresh')
    return Response({'refresh': str(refresh_token)})
