from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    image = models.ImageField(upload_to='services/', verbose_name="صورة الخدمة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
