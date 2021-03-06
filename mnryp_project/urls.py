"""mnryp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import static_pages.views
import categories.views, categories.urls, categories.listing_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', static_pages.views.about, name="about"),
    path('', static_pages.views.home, name="home"),
    path('contact/', static_pages.views.contact, name="contact"),
    path('privacy_policy/', static_pages.views.privacy_policy, name="privacy_policy"),
    path('categories/', include(categories.urls)),
    path('listings/', include(categories.listing_urls)),
    path('accounts/', include('allauth.urls')),
]
