from model.project import Project
from fixture.project import ProjectHelper


def test_add_project(app, json_project):
    project = json_project
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.project.get_project_list()
    print('\n Before = ', app.project.count_projects())
    app.project.create(project)
    print('\n After = ', app.project.count_projects())
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == app.project.count_projects()
    old_projects.append(project)
    sort_old_list = sorted(old_projects, key=Project.name)  # Сортируем старый список
    sort_new_list = sorted(new_projects, key=Project.name)  # Сортируем новый список

    #sorted_old_list = sorted(old_projects)
    #sorted_new_list = sorted(new_projects)
    assert sort_old_list == sort_new_list





