# import webbrowser

# url = "http://www.python.org/"
# webbrowser.open(url)


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import FakeUserAgent
import time


opts = Options()      # instantiate
ua = FakeUserAgent()  # instantiate
url = "http://www.python.org/"
url2 = "https://gs.statcounter.com/detect"
url3 = "https://www.whatismyip.com"


# 還不確定用途 (想換ip)
# proxy = "124.240.187.80:82"
# DesiredCapabilities.EDGE['proxy'] = {
#    "httpProxy":proxy,
#    "ftpProxy":proxy,
#    "sslProxy":proxy,
#    "noProxy":None,
#    "proxyType":"MANUAL",
#    "class":"org.openqa.selenium.Proxy",
#    "autodetect":False
    

# 必要設定
opts.add_argument(f"--user-agent={ua.random}")
opts.add_experimental_option("excludeSwitches", ['enable-automation'])  # 隱藏automation字樣
opts.add_experimental_option("detach", True)  # Keep browser open


# 選用設定
# opts.use_chromium = True
# opts.add_argument("user-data-dir=selenium")                 # 儲存user data
# opts.add_argument("start-maximized")                        # 全視窗
# opts.add_argument("--disable-extensions")                   # 禁用extension
# opts.add_argument("--disable-gpu")                          # 禁用GPU
# opts.add_argument("--disable-dev-shm-usage")                # 使用 /tmp 而非 /dev/shm 作為暫存區
# opts.add_argument("--no-sandbox")                           # 以root身分執行browser
# opts.add_argument("--disable-notifications")
# opts.add_argument("--remote-debugging-port=9222") 
# opts.add_argument("--hide-scrollbars")                      # hide scroll bar
# opts.add_argument("--incognito")                            # 無痕模式
# opts.add_argument("--disable-javascript")                   # 禁用JS
# opts.add_argument("--blink-settings=imagesEnabled=false")   # 不載圖片(加快速度)
# opts.add_argument("--headless")                             # 在無桌面環境下啟動
# opts.add_argument("--proxy-server")                         # 設定連線用的跳板"

# 打開網頁
driver = webdriver.Edge(options=opts, service=Service(executable_path='./msedgedriver.exe'))
driver.get(url)
driver.implicitly_wait(10)  # 10秒內找不到element就報錯NoSuchElementException


# # 定位元素並執行
# Download = driver.find_element(By.XPATH, "//li[@id='downloads']")
# time.sleep(2)
# Download.click()
# time.sleep(2)
# Download2 = driver.find_element(By.XPATH, "//div[@class='download-os-windows']//p[@class='download-buttons']//a[@class='button']") # 下載python(成功!)
# Download2.click()


# # 附加功能
# # element.get_attribute('outerHTML')  取得當前標籤完整HTML













