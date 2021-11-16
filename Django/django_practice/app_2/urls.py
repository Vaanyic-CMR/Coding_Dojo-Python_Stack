from django.urls import path
from . import views

urlpatterns = [
    path( 'app_2/', views.index ),
]