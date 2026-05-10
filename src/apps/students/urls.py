from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

r =DefaultRouter()
r.register("student", StudentViewSet)


urlpatterns = [
    path('', include(r.urls)),
]
