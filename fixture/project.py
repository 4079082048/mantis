from selenium.webdriver.common.by import By
from model.project import Project



__author__ = 'Sofia'



class ProjectHelper:
    def __init__(self, app):
        self.project_cache = None
        self.app = app


    def create(self, new_project):
        # create Project
        wd = self.app.wd
        self.create_project_page()
        self.fill_project_data(new_project)
        self.submit_creation()

    def submit_creation(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//input[@value="Добавить проект"]').click()


    def open_project_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, "//span[text()=' Управление ']").click()
        wd.find_element(By.XPATH, "//a[normalize-space(text())='Проекты']").click()


    def select_project(self):
        wd = self.app.wd
        self.open_project_page()

    def delete_project(self):
        wd = self.app.wd
        self.open_project_page()


    def create_project_page(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[text()='Создать новый проект']").click()


    def fill_project_data(self, new_project):
        wd = self.app.wd
        self.change_filed_value("name",new_project.name)
        self.change_filed_value("description", new_project.description)

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    def username(self):
        wd = self.app.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()


    def get_project_list(self,):
        if self.project_cache is None:
            wd = self.app.wd
            self.project_cache = []
            for element in wd.find_elements(By.NAME, "tr"):
                cells = element.find_elements(By.TAG_NAME, "th")
                name = cells[1].text
                status = cells[2].text
                #id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                view_state =  cells[4].text
                description =  cells[5].text
                self.project_cache.append(Project(name=name, status=status, view_state=view_state, description=description)) # enabled=enabled
        return list(self.project_cache)

    def count_projects(self):
        wd = self.app.wd
        self.open_project_page()
        p = len(wd.find_elements(By.XPATH, '//a[contains(@href,"manage_proj_edit_page.php?project_id")]'))
        return p



