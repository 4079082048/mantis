from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.project import Project
from model.group import Group
import re
__author__ = 'Sofia'


class ProjectHelper():
    def __init__(self, app):
        self.app = app

    contact_cache = None
    def create(self, new_project_data):
        # create Project
        wd = self.app.wd
        self.app.open_project_page()
        wd.find_element(By.XPATH, '//button[normalize-space(text())="Создать новый проект"]')
        self.fill_project_data()
        wd.find_element(By.XPATH, '//div[@id="content"]/form/input[20]').click()
        #self.check_main_page()

    def open_project_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, "//span[text()=' Управление ']").click()
        wd.find_element(By.XPATH, "//a[normalize-space(text())='Проекты']")




    def fill_project_data(self):
        wd = self.app.wd
        self.change_filed_value("name", project.name)
        self.change_filed_value("homepage", contact.homepage)

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)
        self.contact_cache = None




    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, 'input[id="%s"]' % contact_id).click()
        wd.find_element(By.XPATH, '//select[@name="to_group"]/option[contains(@value, "%s")]' % group_id).click()
        wd.find_element(By.XPATH, '//input[@value="Add to"]').click()

    def del_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, '//select[@name="group"]/option[contains(@value, "%s")]' % group_id).click()
        wd.find_element(By.CSS_SELECTOR, 'input[id="%s"]' % contact_id).click()
        wd.find_element(By.XPATH, '//input[@name="remove"]').click()
        self.cont_cache = None


    def username(self):
        wd = self.app.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

