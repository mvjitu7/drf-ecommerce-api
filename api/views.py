from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class GetProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class EditProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class GetCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GetUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer