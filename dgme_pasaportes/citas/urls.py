from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paso1/', views.paso1, name='paso1'),
    path('paso2/', views.paso2, name='paso2'),
    path('paso3/', views.paso3, name='paso3'),
    path('confirmacion/<int:cita_id>/', views.confirmacion, name='confirmacion'),
]
