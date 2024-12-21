from model.project import Project
from fixture.project import ProjectHelper
import random

# Генерируем случайное число
random_number = random.randint(1, 100)  # Вы можете задать любой диапазон

# Создаем имя и описанме проекта с добавлением случайного числа
project_name = f"NewPName{random_number}"
project_desc = f"NewPD{random_number}"
#
def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    app.project.create(Project(name=project_name, description=project_desc))
