from django.shortcuts import render, redirect
from .models import Service
import subprocess

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

def run_script(request, service_id):
    print("🚀 الزر تم الضغط عليه!")

    script_path = f"services/scripts/automation_script.py"
    try:
        subprocess.run(["python", script_path], check=True)
    except Exception as e:
        print(f"[خطأ أثناء تنفيذ السكربت]: {e}")
    return redirect('services:services_list')
