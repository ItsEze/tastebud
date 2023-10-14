from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import SignupSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            User.objects.create_user( username=username, email=email, password=password )