from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    OrderViewSet, TypeServiceView, OrderStatusView,
    ActiveClientOrders, WorkerOrdersViewSet, WorkerActiveOrder, WorkerHistoryOrders, WorkerTodayOrders, OrderInfoView

)

r = DefaultRouter()
r.register('orders', OrderViewSet)
r.register('orders-worker', WorkerOrdersViewSet)

orders_urlpatterns = [
    path('orders/type/', TypeServiceView.as_view()),
    path('orders/status/', OrderStatusView.as_view()),
    path('orders/active/', ActiveClientOrders.as_view()),
    path('order/info/<int:pk>/', OrderInfoView.as_view()),

    path('orders-worker/active/', WorkerActiveOrder.as_view()),
    path('orders-worker/history/', WorkerHistoryOrders.as_view()),
    path('orders-worker/today/', WorkerTodayOrders.as_view())
] + r.urls