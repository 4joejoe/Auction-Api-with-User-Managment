import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import  Response
from rest_framework.views import APIView
from users import serializers
from users.models import MyUser
from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserSerializer
from .forms import UserRegisterForm
from django.contrib import messages
from django.urls import reverse
from .admin import UserCreationForm
from django.shortcuts import render, redirect, reverse
import pandas as pd


# CRUD

# Create
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Read
class LoginView(APIView):
    def post(self, request):
        # user_object = MyUser.objects.values()
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            permmissons = {}
            permmissons['is_admin']=request.user.is_admin
            permmissons['is_active']=request.user.is_active


            return Response({'msg': 'Login Success',"username":request.user.username,"permmissons":permmissons, **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Update
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True) #Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response({'msg': 'Password Changed'},status=status.HTTP_204_NO_CONTENT)

# Delete
class DeleteUser(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer
    
    def delete(self,request,username):
        # username = request.POST['username']
        # print("BOOM",user_to_delete)
        user_to_delete = MyUser.objects.get(username=username)
        user_to_delete.delete()
        return Response({"Deleted User":username})
    
# Read
class AllUser(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self,request):
        get_all_user = MyUser.objects.values()
        data = pd.DataFrame(get_all_user)
        data = data[['email','username','is_admin','is_staff']]
        print(f"--- {data.columns}")
        return Response(json.loads(data.to_json(orient='records')))


class LogoutView(APIView):
    def post(self,request):
        logout(request)
        return redirect('/accounts/login')

