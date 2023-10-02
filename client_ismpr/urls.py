from django.urls import include, path
from .views import RegisterNewUserView, AuthUserView, EquipmentClientView


user_urlpatterns = [
    path('register/', RegisterNewUserView.as_view()),
    path('auth/', AuthUserView.as_view()),

    path('equipment/', EquipmentClientView.as_view())
]