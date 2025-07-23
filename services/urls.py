# services/urls.py
from django.urls import path
from . import views

app_name = 'services'  # مهم جداً

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('run/<int:service_id>/', views.run_script, name='run_script'),  # الزر يعتمد على هذا
]
