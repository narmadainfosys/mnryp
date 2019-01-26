from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path('create/', views.create, name="create"),
    path('<str:slug>/', views.listing, name="listing"),
]
