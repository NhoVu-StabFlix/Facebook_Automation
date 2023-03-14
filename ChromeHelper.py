import time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import pyotp


class ChromeHelper():
    def __init__(self):
        """ add options and init chromedriver"""
        options = uc.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--app=https://iphey.com/")
        self.driver = uc.Chrome(options=options)

    def get_driver(self):
        return self.driver

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).click()
        except:
            print("khong tim thay elemnt click")

    def do_sendkeys(self, by_locator, text):
        try:

            for t in text:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).send_keys(t)
                time.sleep(0.25)

        except:
            print("element not founded")

    def is_element_visiable(self, by_locator):
        try:

            element = WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(by_locator))
            return element
        except:
            print("element not founded")

    def get_page_source(self, current_url):
        try:

            element = self.driver.page_source(current_url)
            return element
        except:
            print("get source page error")

    def get_cookies(self):
        try:
            element = self.driver.get_cookies()
            return element
        except:
            print("get cookies error")

    def do_clear_text(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).clear()
            return
        except:
            print("element not founded")

    def getOTP2FA(self, key):
        try:
            totp = pyotp.TOTP(key)
            digit_code=totp.now()
            print("Current OTP:", digit_code)
            return digit_code

        except:
            print("get 2fa error")
