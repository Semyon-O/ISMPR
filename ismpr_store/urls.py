from django.urls import path

from ismpr_store import views

store_urlpatterns = [
    path('/', views.InfoAboutStore.as_view()),
    path('/<pk>/spare-parts/', views.RetrieveAllSparePartsByConcreteStore.as_view()),
    path('/<pk>/', views.RetrieveConcreteStore.as_view()),
]