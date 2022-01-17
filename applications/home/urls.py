from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='iniciar_sesion'),
    path('mixin/', views.TemplatePruebaMixin.as_view(), name='mixin')
]
