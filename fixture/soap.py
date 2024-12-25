from urllib.request import localhost
from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self,app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.26.4/api/soap/mantisconnect.wsdl") #???
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_soap_list(self, username, password):
        client = Client('http://localhost/mantisbt-2.26.4/api/soap/mantisconnect.wsdl')
        project_list = client.service.mc_projects_get_user_accessible(username, password)
        return project_list

