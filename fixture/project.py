from selenium.webdriver.common.by import By
from model.project import Project


__author__ = 'Sofia'


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self):
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
        self.change_filed_value("name", )
        self.change_filed_value("description",)
        #self.change_filed_value("status", project.status)
        #self.change_filed_value("inherit_global", project.inherit_global)
        #self.change_filed_value("view_state", project.view_state)

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)
        self.contact_cache = None





    def username(self):
        wd = self.app.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()



