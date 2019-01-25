from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path('<str:slug>/', views.listing, name="listing"),
]
