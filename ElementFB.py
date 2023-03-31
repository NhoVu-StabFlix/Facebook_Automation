from selenium.webdriver.common.by import By

""""FACEBOOK TEMPLATE"""
EMAIL_INPUT = (By.XPATH, "//input[@id='m_login_email']")
PASSWORD_INPUT = (By.XPATH, "//input[@id='m_login_password']")
LOGIN_BUTTON = (By.XPATH,
                "//body/div[@id='viewport']/div[@id='page']/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[3]/form[1]/div[5]/div[1]/button[1]")
FORGET_PASSWORD_BUTTON = (By.XPATH, "//a[starts-with(@id,'forgot-password-link')]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[starts-with(@id,'signup-button')]")
CHECKPOINT_URL = "https://m.facebook.com/checkpoint/?next"
APPROVALS_CODE = (By.ID, "approvals_code")
SUBMIT_BUTTON = (By.ID, "checkpointSubmitButton")
NEWSFEED ="//div[@id='m_news_feed_stream']/descendant::article"
post="//div[@id='m_news_feed_stream']/descendant::article[{}]"
TEXT_POST="//div[@id='m_news_feed_stream']/descendant::article/descendant::div[@data-ft='{'tn':'*s'}']"
FRIEND_BUTTON=(By.XPATH,"//div[@id='requests_jewel']/a")
ADD_FRIEND_BUTTON="//button[@value='Thêm bạn bè']"
SUGESSTION_FRIEND=(By.XPATH,"//a[contains(@href,'/friends/center/suggestions')]")
LIKE_BUTTON = (By.XPATH, "Thích")













"""SHOPEE TEMPLATE"""
BANNER_ADS = (By.CLASS_NAME, "simple-banner with-placeholder")
CLOSE_ADS = (By.CLASS_NAME, "shopee-popup__close-btn")
LOGIN_SHOPEE_BUTTON = (By.XPATH,
                       "//a[@class='navbar__link navbar__link--account navbar__link--login navbar__link--tappable navbar__link--hoverable navbar__link-text navbar__link-text--medium navbar__link-text--normal-case']")
LOGIN_BY_FB_BUTTON = (By.XPATH,
                   "//button//div[contains(text(),'Facebook')]")
CONTINUE_BUTTON=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
USER_SHOPEE_BUTTON=(By.CLASS_NAME,"navbar__username")

""""TIKTOK TEMPLATE"""
LOGIN_TIKTOK_BUTTON=(By.XPATH,"//button[@data-e2e='top-login-button']")
LOGIN_TIKTOK_BY_FB_BUTTON=(By.XPATH,"//div[@data-e2e='channel-item']//p[text()='Continue with Facebook']")
PASSWORD_INPUT_LOGIN_TIKTOK=(By.XPATH,"//input[@name='pass']")
CONTINUE_FB_TIKTOK_BUTTON=(By.XPATH,"//input[@type='submit']")

""""LAZADA TEMPLATE"""
LOGIN_LAZ_BUTTON=(By.XPATH,"//div[@id='anonLogin']")
LOGIN_LAZ_BY_FB_BUTTON=(By.XPATH,"//button[@class='mod-button mod-button mod-third-party-login-btn mod-third-party-login-fb']")