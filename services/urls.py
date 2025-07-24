# services/urls.py
from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('run/<int:service_id>/', views.run_script, name='run_script'),
    path('execute-login/', views.execute_login_script, name='execute_login_script'),
    path('submit_otp/', views.submit_otp, name='submit_otp'),  # ✅ أضف هذا السطر
]
