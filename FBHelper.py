import time
from ChromeHelper import ChromeHelper as Chrome
from ElementFB import *


class FBHelper(Chrome):
    def __init__(self):
        Chrome.__init__(self)
        self.username = "100084219480623"
        self.password = "tjipec6742yiflv"
        self.twoauth = "ISLXEVFQUBBKDGCMKGLGM7TFR4GIFE3T"
        self.r_cookies = "r_cookies"

    def login(self):
        time.sleep(10)
        try:
            self.driver.get("https://m.facebook.com")
            print(self.username)
            time.sleep(5)
            self.do_sendkeys(EMAIL_INPUT, self.username)
            time.sleep(3)
            self.do_sendkeys(PASSWORD_INPUT, self.password)
            time.sleep(5)
            self.do_click(LOGIN_BUTTON)
            time.sleep(10)
        except:
            print("login fail")
        """Check 2FA and Input digit code"""
        try:
            current_url = self.driver.current_url
            print(current_url)
            if "/checkpoint" in current_url:
                OTP = self.getOTP2FA(self.twoauth)
                time.sleep(10)
                self.do_sendkeys(APPROVALS_CODE, OTP)
                self.do_click(SUBMIT_BUTTON)

        except:
            pass
        time.sleep(10)

        while True:
            current_url = self.driver.current_url
            if not "checkpoint" in current_url:
                break
            try:
                time.sleep(3)
                self.do_click(SUBMIT_BUTTON)
            except:
                pass

        time.sleep(10)

    def check_login(self):
        self.login_cookie = ''
        for cookie in self.driver.get_cookies():
            self.login_cookie += cookie['name'] + '=' + cookie['value'] + ';'

        print(self.login_cookie)
        if "c_user=" in self.login_cookie:
            print("login success")
            return True
        print("login fail")
        return False

    def surf_newsfeed(self):
        pass

    def add_friend(self):
        pass

    def watch_video(self):
        pass

    def up_story(self):
        pass
