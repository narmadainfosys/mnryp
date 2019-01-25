from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name="categories"),
    path('<str:slug>/', views.category, name="category"),
]
