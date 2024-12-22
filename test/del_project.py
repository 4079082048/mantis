from model.project import Project
from fixture.project import ProjectHelper
import random

# Генерируем случайное число
random_number = random.randint(1, 100)  # Вы можете задать любой диапазон

# Создаем имя и описанме проекта с добавлением случайного числа
project_name = f"NewPName{random_number}"
project_desc = f"NewPD{random_number}"
#


def test_del_project(app):
    if app.contact.count() == 0:
        app.contact.create(Project(name=project_name, description=project_desc))
    old_projects = app.project.get_project_list()
    app.session.login("administrator", "root")
