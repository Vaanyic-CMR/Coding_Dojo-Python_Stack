from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index),
    path( 'add', views.add ),
    path( 'destroy_session', views.destroy_session ),
]