from selenium.webdriver.common.by import By
import re

class SignupHelper:
    def __init__(self,app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.baseUrl + "/signup_page.php")
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.NAME, "email").send_keys(email)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        mail = self.app.mail.get_email("")
        url = self.extract_confirmation_url(mail)

        wd.get(url)
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def extract_confirmation_url(self, text):
        re.search("http://.*$", text).group(0)




