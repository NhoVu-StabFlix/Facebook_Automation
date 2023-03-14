from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.XPATH, "//input[@id='m_login_email']")
PASSWORD_INPUT = (By.XPATH, "//input[@id='m_login_password']")
LOGIN_BUTTON = (By.XPATH,"//body/div[@id='viewport']/div[@id='page']/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[3]/form[1]/div[5]/div[1]/button[1]")
FORGET_PASSWORD_BUTTON = (By.XPATH, "//a[starts-with(@id,'forgot-password-link')]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[starts-with(@id,'signup-button')]")
CHECKPOINT_URL = "https://m.facebook.com/checkpoint/?next"
APPROVALS_CODE = (By.ID, "approvals_code")
SUBMIT_BUTTON=(By.ID,"checkpointSubmitButton")

