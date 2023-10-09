from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

r = DefaultRouter()
r.register('orders', OrderViewSet)

orders_urlpatterns = r.urls