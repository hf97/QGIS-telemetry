from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jsonfile', views.jsonfile, name='jsonfile'),
]