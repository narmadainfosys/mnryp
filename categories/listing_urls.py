from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.listings, name="listings"),
    path('results/', views.search, name="search"),
    path('create/', views.create_listing, name="create_listing"),
    path('<slug:slug>/', views.listing, name="listing"),
    path('<slug:slug>/edit', views.edit_listing, name="edit_listing"),
    path('<slug:slug>/delete', views.delete_listing, name="delete_listing"),
]
