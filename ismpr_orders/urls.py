from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, TypeServiceView, OrderStatusView, ActiveClientOrders

r = DefaultRouter()
r.register('orders', OrderViewSet)

orders_urlpatterns = [
    path('orders/type/', TypeServiceView.as_view()),
    path('orders/status/', OrderStatusView.as_view()),
    path('orders/active/', ActiveClientOrders.as_view())
] + r.urls