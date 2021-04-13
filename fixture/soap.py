from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def wsdl_client(self):
        return Client(self.app.base_url + self.app.config['web']['wsdl'])


    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_projects_list(self):
        list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            data = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                      self.app.config['webadmin']['password'])
            for row in data:
                id = row["id"]
                name = row["name"]
                description = row["description"]
                list.append(Project(id=id, name=name, description=description))
            return list
        except WebFault:
            return False