from django.urls import path
from . import views

app_name = "categories"
urlpatterns = [
    path('', views.categories, name="categories"),
    path('<slug:slug>/', views.category, name="category"),
]
