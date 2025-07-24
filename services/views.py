# services/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
import subprocess
import os
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

def run_script(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/fill_credentials.html', {'service': service})

@csrf_exempt
def execute_login_script(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ طباعة البيانات للتأكد من وصولها
        print("📥 تم استلام بيانات تسجيل الدخول:")
        print("🟢 اسم المستخدم:", username)
        print("🟢 كلمة المرور:", password)

        script_path = os.path.join(settings.BASE_DIR, 'services', 'scripts', 'absher_login.py')

        try:
            # ✅ تمرير البيانات إلى سكربت Selenium
            subprocess.Popen(['python', script_path, username, password], shell=True)
            print(f"✅ تم تشغيل السكربت بنجاح لـ {username}")
        except Exception as e:
            print(f"❌ خطأ أثناء تشغيل السكربت: {e}")

    return redirect('services:services_list')

@csrf_exempt
def submit_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp_code')

        script_path = os.path.join(settings.BASE_DIR, 'services', 'scripts', 'submit_otp.py')
        try:
            subprocess.Popen(['python', script_path, otp], shell=True)
            print(f"✅ تم تمرير رمز التحقق: {otp}")
        except Exception as e:
            print(f"❌ خطأ أثناء تمرير رمز التحقق: {e}")
    
    return redirect('services:services_list')
