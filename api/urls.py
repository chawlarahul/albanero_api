from django.conf.urls import url, include
from django import views
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'albanero', viewsets.ProcessFileViewset, basename='albanero')


urlpatterns = [
    url(r'', include(router.urls)),
]