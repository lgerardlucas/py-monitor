from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app_monitor.api.viewsets import MonitorViewSet

router = routers.DefaultRouter()
router.register(r'monitor', MonitorViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
