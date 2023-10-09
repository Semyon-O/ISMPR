from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ismpr_worker.views import AuthWorkerView


worker_urlpatterns = [
    path('auth/', AuthWorkerView.as_view()),
]