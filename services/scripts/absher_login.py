import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_absher(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=ar")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    try:
        print("🚀 فتح موقع أبشر...")
        driver.get("https://www.absher.sa/wps/portal/individuals/Home/homepublic")
        print("✅ تم فتح موقع أبشر")

        # فقط الدخول إلى صفحة تسجيل الدخول بدون الضغط على زر تسجيل الدخول في الموقع
        print("➡️ الانتقال اليدوي إلى صفحة تسجيل الدخول...")
        driver.get("https://www.absher.sa/wps/portal/individuals/login")
        print("✅ تم الدخول إلى صفحة تسجيل الدخول مباشرة")

        # انتظار الحقول
        print("⏳ انتظار ظهور الحقول...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div[2]/div/div/div[1]/section/div[2]/div/div/div/form/div[1]/div[2]/div[1]/div/input'))
        )

        # طباعة القيم المستلمة
        print("🟢 اسم المستخدم:", username)
        print("🟢 كلمة المرور:", password)

        # تعبئة الحقول
        user_input = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[1]/section/div[2]/div/div/div/form/div[1]/div[2]/div[1]/div/input')
        pass_input = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[1]/section/div[2]/div/div/div/form/div[1]/div[2]/div[2]/div/input')

        user_input.clear()
        user_input.send_keys(username)
        pass_input.clear()
        pass_input.send_keys(password)
        driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/section/div[2]/div/div/div/form/div[2]/input").click()

        print("✅ تم إدخال البيانات بنجاح في موقع أبشر ✅")

        # الانتظار لفحص العملية يدويًا
        time.sleep(15)

    except Exception as e:
        print(f"❌ حدث خطأ أثناء التنفيذ: {e}")

    finally:
        print("🧹 إغلاق المتصفح...")
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❌ يجب تمرير اسم المستخدم وكلمة المرور كوسيطين")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    login_absher(username, password)
