from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:
    def __init__(self,app):
        self.app = app

    def can_login(self, username, password):
        #client = Client("http://localhost/mantisbt-2.26.4/api/soap/mantisconnect.php?wsdl")
        client = Client(self.app.base_url + '/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_soap_list(self, username, password):
        #client = Client('http://localhost/mantisbt-2.26.4/api/soap/mantisconnect.php?wsdl')
        client = Client(self.app.base_url + '/api/soap/mantisconnect.php?wsdl')
        project_list = client.service.mc_projects_get_user_accessible(username, password) #что-то с проджект словом
        return self.convert_list(project_list)



    def convert_list(self, project_list):
        def convert(x):
            return Project(name=x.name, description=x.description)
        result = [convert(z) for z in project_list]
        return sorted(result, key=lambda project: project.name)



