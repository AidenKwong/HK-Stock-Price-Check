from django.urls import path
from . import views

urlpatterns = [
    path("getstock", views.getstock, name="getstock"),
]
