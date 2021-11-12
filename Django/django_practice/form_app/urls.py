from django.urls import path
from . import views

urlpatterns = [
    path( 'form_app/', views.index ),
    path( 'form_app/users', views.create_user ),
    path('form_app/success', views.success),
]