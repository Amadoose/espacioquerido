from django.urls import path
from . import views    

app_name = 'espacioquerido'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('properties/', views.properties, name='properties'),
    path('clients/', views.clients, name='clients'),
    path('agents/', views.agents, name='agents'),
    path('transactions/', views.transactions, name='transactions'),
    path('reports/', views.reports, name='reports'),
]


