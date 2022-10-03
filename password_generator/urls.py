from django.urls import path
from . import views # import views.py models so that we can use functions/classed defined in views.py

urlpatterns = [
    path("", views.home, name = 'generator-home'), 
    path("password/", views.password, name = 'generator-password'), 
]