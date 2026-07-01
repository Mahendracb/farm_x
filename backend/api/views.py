import os
import requests
from google import genai

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Crop, Scheme, Buyer
from .serializers import CropSerializer, SchemeSerializer, BuyerSerializer
class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        identifier = request.data.get("username")
        password = request.data.get("password")

        if not identifier or not password:
            return Response({"error": "Username/email/full name and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        identifier = identifier.strip()
        query = Q(username=identifier) | Q(email=identifier)
        name_parts = identifier.split()
        if len(name_parts) >= 2:
            first = name_parts[0]
            last = ' '.join(name_parts[1:])
            query |= Q(first_name__iexact=first, last_name__iexact=last)

        user = User.objects.filter(query).first()

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username, "email": user.email, "first_name": user.first_name, "last_name": user.last_name})

        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "This account already exists. Please login."}, status=status.HTTP_400_BAD_REQUEST)

        email = username if "@" in username else ""
        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)


class AITextView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        prompt = request.data.get("prompt", "").strip()

        if not prompt:
            return Response(
                {"error": "Prompt is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            client = genai.Client(
                api_key=settings.GOOGLE_API_KEY
            )

            response = client.models.generate_content(
    model=settings.GOOGLE_MODEL,
    contents=f"""
         You are an agricultural expert.

              First answer in simple English.
         Then provide the same answer in simple Kannada.
          Keep both answers short and easy to understand.
           Avoid technical terms.

            Question:
              {prompt}
                 """
                 )

            return Response({
                "result": response.text
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserProfileView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "date_joined": user.date_joined
        })

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)