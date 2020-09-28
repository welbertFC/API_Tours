"""API_Tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from tourist_point.api.viewsets import TouristPointViewSet
from attractions.api.viewsets import AttractionsViewSet
from location.api.viewsets import LocationViewSet
from commentreview.api.viewsets import CommentReviewViewSet
from evaluation.api.viewsets import EvaluationViewSet
from django.contrib.auth.models import User


from django.conf.urls import include

routers = routers.DefaultRouter()
routers.register(r'touristpoint', TouristPointViewSet)
routers.register(r'attractions', AttractionsViewSet)
routers.register(r'location', LocationViewSet)
routers.register(r'comment', CommentReviewViewSet)
routers.register(r'evaluation', EvaluationViewSet)
routers.register(r'user', User)




urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
]
