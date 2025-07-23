from django.db import models

# لاحقًا يمكن إنشاء نموذج لنتائج الخدمات مثلاً، لكن حالياً نتركه فارغًا أو نضع نموذجًا تجريبيًا

class Placeholder(models.Model):
    message = models.CharField(max_length=100, default="نموذج تجريبي")

    def __str__(self):
        return self.message
