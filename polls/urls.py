from django.urls import path
# from django.utils import 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]