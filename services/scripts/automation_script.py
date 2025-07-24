from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def open_absher():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=ar")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    try:
        absher_url = "https://www.absher.sa/wps/portal/individuals/Home/homepublic"
        driver.get(absher_url)
        print("✅ تم فتح موقع أبشر بنجاح")
        time.sleep(10)  # ابقَ في الصفحة 10 ثوانٍ فقط (يمكنك زيادتها)

    except Exception as e:
        print(f"❌ حدث خطأ أثناء فتح الموقع: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    open_absher()
