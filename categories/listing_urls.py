from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path('create/', views.create_listing, name="create_listing"),
    path('<str:slug>/', views.listing, name="listing"),
]
