import pytest
from data.project import testdata
from model.project import Project


@pytest.mark.parametrize("project", testdata)
def test_compare_list_soap(app, project, config):
 #надо вынести куда-то в тесты отдельно, но сил уже нет
    username = config["web_admin"]['username']
    password = config["web_admin"]['password']
    app.session.login("administrator", "root")

    app.project.open_project_page()
    old_projects = app.soap.get_project_soap_list(username, password)
    app.project.create(project)
    new_projects = app.soap.get_project_soap_list(username, password)
    assert len(old_projects) + 1 == app.project.count_projects()
    old_projects.append(project)
    sort_old_list = sorted(old_projects, key=Project.name)
    sort_new_list = sorted(new_projects, key=Project.name)
    assert sort_old_list == sort_new_list