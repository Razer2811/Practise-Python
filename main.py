from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# ==============================
# Cấu hình Chrome
# ==============================
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# (Tuỳ chọn) Dùng profile thật để tăng độ tin cậy
# options.add_argument(r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
# options.add_argument("profile-directory=Default")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Xóa cờ navigator.webdriver
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
    """
})

# ==============================
# Mở Google
# ==============================
driver.get("https://google.com")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# ==============================
# Tìm kiếm với hành vi giống người
# ==============================
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()

search_query = "tech with tim"
for ch in search_query:
    input_element.send_keys(ch)
    time.sleep(random.uniform(0.15, 0.35))  # delay ngẫu nhiên

input_element.send_keys(Keys.ENTER)

# ==============================
# Chờ kết quả và click link
# ==============================
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

# Giả lập cuộn trang để giống người
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(random.uniform(1, 2))

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

# ==============================
# Dừng lại để xem kết quả
# ==============================
time.sleep(30)
driver.quit()
