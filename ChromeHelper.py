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
from selenium_stealth import stealth
import pyotp
import random


class ChromeHelper():
    def __init__(self):
        """ add options and init chromedriver"""
        options = uc.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--profile-directory=Default")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('disable-geolocation')
        options.add_argument('ignore-certificate-errors')
        options.add_argument('disable-popup-blocking')
        options.add_argument('disable-web-security')
        options.add_argument('disable-translate')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--app=https://abrahamjuliot.github.io/creepjs/')
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    def get_driver(self):
        return self.driver

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).click()
        except NoSuchElementException:
            print("element not founded")

    def do_sendkeys(self, by_locator, text):
        try:

            for t in text:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).send_keys(t)
                time.sleep(0.25)

        except NoSuchElementException:
            print("element not founded")

    def is_element_visiable(self, by_locator):
        try:

            element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(by_locator))
            return element
        except:
            pass

    def get_page_source(self, current_url):
        try:

            element = self.driver.page_source(current_url)
            return element
        except NoSuchElementException:
            print("get source page error")

    def get_cookies(self):
        try:
            element = self.driver.get_cookies()
            return element
        except NoSuchElementException:
            print("get cookies error")

    def do_clear_text(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).clear()
            return
        except NoSuchElementException:
            print("element not founded")

    def getOTP2FA(self, key):
        try:
            totp = pyotp.TOTP(key)
            digit_code = totp.now()
            print("Current OTP:", digit_code)
            return digit_code

        except NoSuchElementException:
            print("get 2fa error")

    def wait_page_load(self):
        while True:
            x = self.driver.execute_script("return document.readyState")
            if x == "complete":
                return True
            else:
                yield False

    def scroll_to_Element(self, by_locator):
        try:
            element = by_locator
            ActionChains(self.driver).scroll_to_element(element).perform()

        except:
            pass

    def find_all_element(self, by_locator):

        elements = self.driver.find_elements(By.XPATH, by_locator)

        return elements

    def find_child_element(self,element,by_locator):
        child=element.find_element(by_locator)
        return child
    def open_new_tab(self):
        try:
            self.driver.switch_to.new_window('tab')

            return self.driver.current_window_handle

        except:
            pass

    def random_click(self):
        x = 1
        y = 1
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y)
        actions.click()
        actions.perform()

    def move_to_click(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(by_locator))
        action = ActionChains(self).move_to_element(element)
        action.click()
        action.perform()

    def switch_to_tab(self):
        for win_handle in self.driver.window_handles:
            self.driver.switch_to.window(win_handle)
