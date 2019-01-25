from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name="categories"),
    # This one is old- path('^category/(?P<slug>[-\w]+)/', iews.category, name="category"),
    #make it so that slug can carry other things than intigers
    path('<str:slug>/', views.category, name="category"),

]
