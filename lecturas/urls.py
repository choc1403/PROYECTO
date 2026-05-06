# URL
from django.urls import path, include

# Views
from . import views

# FILTROS

# Decorador
from django.contrib.auth.decorators import login_required

# Routes
from .api import routers


app_name = 'lecturas'

urlpatterns = [
    
]

urlpatterns+=routers.urlpatterns