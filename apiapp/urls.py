from django.contrib import admin
from django.urls import path, include
from . import views
from . import models
from rest_framework import routers

router = routers.DefaultRouter()
router.register('heroes', views.HeroViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
