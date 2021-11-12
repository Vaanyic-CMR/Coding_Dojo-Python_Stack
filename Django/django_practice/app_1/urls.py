from django.urls import path
from . import views

urlpatterns = [
    path( 'app_1/', views.index ),
]