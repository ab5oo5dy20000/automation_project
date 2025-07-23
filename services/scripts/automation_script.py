# services/scripts/automation_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_google_search():
    # ✅ إعداد خيارات المتصفح
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # فتح المتصفح بوضع ملء الشاشة
    # options.add_argument("--headless")  # ← يمكنك تفعيل هذا للسيرفرات بدون واجهة رسومية

    # ✅ تشغيل المتصفح
    driver = webdriver.Chrome(options=options)

    try:
        # 🔍 التوجه إلى صفحة Google
        driver.get("https://www.google.com")

        # 🔎 العثور على مربع البحث
        search_box = driver.find_element(By.NAME, "q")

        # 📝 إدخال كلمة البحث
        search_term = "أتمتة الخدمات"
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        # ⏳ الانتظار لظهور النتائج
        time.sleep(5)

    except Exception as e:
        print(f"[خطأ] حدث استثناء أثناء تنفيذ البحث: {e}")

    finally:
        # ✅ إغلاق المتصفح في كل الحالات
        driver.quit()

# ✅ تشغيل الدالة إذا تم تنفيذ السكربت بشكل مباشر
if __name__ == "__main__":
    run_google_search()
