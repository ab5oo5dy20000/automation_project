"""
URL configuration for automation_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ربط تطبيق الخدمات المؤتمتة
    path('services/', include('services.urls', namespace='services')),


    # ربط تطبيق الواجهة - الصفحة الرئيسية
    path('', include('dashboard.urls', namespace='dashboard')),
]

# دعم عرض ملفات media و static أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
