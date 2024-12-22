from model.project import Project
from fixture.project import ProjectHelper
import random
from model.project import Project
from fixture.project import ProjectHelper
import random
from random import randrange


def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    #old_projects = app.project.get_project_list()

    # Проверяем, есть ли проекты в списке
    #if len(old_projects) == 0:
         #Создаем новый проект, если список пуст
    #    app.project.create(Project(name="tpN-97-", description="tpD;gajdlgkr7-9-"))
    old_projects = app.project.get_project_list()  # Обновляем список проектов
    #print("Old projects:", old_projects)  # Для отладки
    index = random.randrange(len(old_projects))
    #print('\n Before = ', app.project.count_projects())
    app.project.delete_project(index)
    #print('\n After = ', app.project.count_projects())

    # Проверяем, что количество проектов уменьшилось на 1
    #assert len(old_projects) - 1 == app.project.count_projects()

    new_projects = app.project.get_project_list()
    old_projects[index:index + 1] = []  # Удаляем проект из старого списка
    sort_old_list = sorted(old_projects)  # Сортируем старый список
    sort_new_list = sorted(new_projects)  # Сортируем новый список

    # Проверяем, что списки совпадают
    assert sort_old_list == sort_new_list
