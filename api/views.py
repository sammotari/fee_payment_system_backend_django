# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, StudentSerializer
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Student

from django.http import JsonResponse
from .utils import get_access_token, mpesa_stk_push

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({'email': user.email}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)

class UserDetailsView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            student = Student.objects.get(user=user)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            student = Student.objects.get(user=user)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


def initiate_mpesa_payment(request):
    consumer_key = "YourConsumerKey"
    consumer_secret = "YourConsumerSecret"
    access_token = get_access_token(consumer_key, consumer_secret)
    phone_number = "254712345678" # Example phone number
    amount = "100" # Example amount
    callback_url = "https://yourdomain.com/mpesa/callback" # Your callback URL

    response = mpesa_stk_push(access_token, phone_number, amount, callback_url)
    return JsonResponse(response)



def mpesa_callback(request):
    # Process the callback data
    # This is where you'll typically update your database with the transaction status
    return JsonResponse({"status": "success"})


