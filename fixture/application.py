from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from selenium import webdriver
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper

__author__ = 'Sofia'

class Application:
    def __init__(self, browser, config): #(self)
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.current_url = None
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.open_home_page()
        self.james =JamesHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        #username = config["web_admin"]['username']
        #password = config["web_admin"]['password']
        #app.session.login("administrator", "root")


    def destroy(self):
        self.wd.quit()


    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return



