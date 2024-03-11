from unicodedata import name
from django.urls import path, include

from . import views

urlpatterns = [
    #index page
    path('', views.index, name='index'),
    path('pag2/', views.pag2, name='pag2'),
]