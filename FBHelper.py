import time
from ChromeHelper import ChromeHelper as Chrome
from ElementFB import *
import random
from facebook_scraper import get_photos, get_posts, get_profile, write_posts_to_csv


class FBHelper(Chrome):
    def __init__(self):
        Chrome.__init__(self)
        self.username = "100085733288952"
        self.password = "enryyt9590cxeeu"
        self.twoauth = "LWKFE3WZKKEHK7H4BWAKEGOWRECXSZ3Y"
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
            time.sleep(5)
            self.wait_page_load()
        except:
            print("login fail")
        """Check 2FA and Input digit code"""
        try:
            current_url = self.driver.current_url
            print(current_url)
            if self.is_element_visiable(APPROVALS_CODE):
                OTP = self.getOTP2FA(self.twoauth)
                time.sleep(10)
                self.do_sendkeys(APPROVALS_CODE, OTP)
                self.do_click(SUBMIT_BUTTON)
                time.sleep(5)
                self.wait_page_load()

        except:
            pass

        self.wait_page_load()

        while True:

            current_url = self.driver.current_url
            if not "checkpoint" in current_url:
                break
            try:
                time.sleep(3)
                self.do_click(SUBMIT_BUTTON)
                self.wait_page_load()
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
        try:
            posts = []
            newsfeeds = self.find_all_element(NEWSFEED)
            if newsfeeds:
                for item in newsfeeds:
                    posts.append(item)

            for post in posts:
                print(post)
                self.scroll_to_Element(post)
                time.sleep(random.randint(5, 10))
            time.sleep(10)

        except:
            print("not found post in newsfeed")

    def add_friend(self):
        list_friend = []

        self.driver.get("https://m.facebook.com")
        self.wait_page_load()

        try:
            self.do_click(FRIEND_BUTTON)
            self.wait_page_load()
            self.do_click(SUGESSTION_FRIEND)
            self.wait_page_load()
        except:
            self.driver.get("https://m.facebook.com/friends/center/suggestions/")

        self.wait_page_load()
        elements = self.find_all_element(ADD_FRIEND_BUTTON)
        for element in elements:
            list_friend.append(element)
            print(element)
        time.sleep(4)
        for friend in list_friend:
            self.scroll_to_Element(friend)
            time.sleep(3)
            self.do_click(friend)
            print("add friend successfully")
            time.sleep(random.randint(5,10))


    def watch_video(self):
        pass

    def up_story(self):
        pass

    def login_shopee(self):
        time.sleep(30)
        self.driver.get("https://shopee.vn/buyer/login")
        time.sleep(5)
        self.wait_page_load()
        self.do_click(LOGIN_BY_FB_BUTTON)
        time.sleep(5)
        self.wait_page_load()
        self.switch_to_tab()
        self.wait_page_load()

        if self.is_element_visiable(CONTINUE_BUTTON):
            self.do_click(CONTINUE_BUTTON)

        time.sleep(10)

    def check_login_shopee(self):

        try:
            if self.is_element_visiable(USER_SHOPEE_BUTTON):
                print("Login Shopee Success")
                return True

        except:
            pass
        print("Login Shopee Fail")
        return False

    def login_tiktok(self):
        self.driver.get("https://www.tiktok.com/login")
        self.do_click(LOGIN_TIKTOK_BY_FB_BUTTON)
        time.sleep(10)
        self.switch_to_tab()
        self.wait_page_load()
        self.do_click(CONTINUE_FB_TIKTOK_BUTTON)
        time.sleep(3)
        self.wait_page_load()
        self.do_click(CONTINUE_BUTTON)
        time.sleep(10)

    def check_login_tiktok(self):
        pass

    def login_lazada(self):
        self.wait_page_load()
        self.driver.get("https://lazada.vn")
        self.wait_page_load()
        self.do_click(LOGIN_LAZ_BUTTON)
        time.sleep(5)
        self.wait_page_load()
        self.do_click(LOGIN_LAZ_BY_FB_BUTTON)
        self.wait_page_load()
        self.switch_to_tab()
        time.sleep(10)
