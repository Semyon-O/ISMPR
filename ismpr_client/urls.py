from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RegisterNewUserView, AuthUserView, EquipmentClientViewSet

r = DefaultRouter()
r.register('equipments', EquipmentClientViewSet)

user_urlpatterns = [
    path('register/', RegisterNewUserView.as_view()),
    path('auth/', AuthUserView.as_view()),
] + r.urls