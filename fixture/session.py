from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author_ = 'Sofia'

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        #  login
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "username").click()
        wd.find_element(By.NAME, "username").clear()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.XPATH, "//input[@type='Submit']").click()


    def logout(self):
        wd = self.app.wd
        # Ожидание появления элемента "Logout"
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.NAME, "user").click()

    def ensure_logout(self):
        wd =self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, "/html/body/div/div[1]/form/a")) > 0

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, '//div[@id="top"]/form/b').text[1:-1]

