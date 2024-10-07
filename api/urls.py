from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.GetProducts.as_view()),
    path('products/<int:pk>/', views.EditProduct.as_view()),

    path('categories/', views.GetCategories.as_view()),
    path('categories/<int:pk>/', views.EditCategory.as_view()),

    path('sellers/', views.GetUsers.as_view()),
    path('sellers/<int:pk>/', views.GetUser.as_view()),
]
