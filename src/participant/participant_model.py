from datetime import datetime
from flask import current_app as app

from src.authserver.authserver_model import AuthorisationServer

class Participant:
    __attributes__ = ['_id', 'OrganisationId', 'OrganisationName', 'LegalEntityName', 'AuthorisationServers']
    __collection__ = 'participants'

    def __init__(self):
        self._id: str
        self.OrganisationId = ""
        self.LegalEntityName = ""
        self._setAuthorisationServers()

    def _setAuthorisationServers(self, servers = []):
        auth_servers = []

        for server in servers:
            auth_server = AuthorisationServer()
            auth_server.from_mapping(server)
            auth_servers.append(auth_server)

        self.AuthorisationServers = auth_servers

        return self.AuthorisationServers
    
    def from_mapping(self, mapping = dict()):
        _mapping = dict()
        for key, value in mapping.items():
            if key in self.__attributes__:
                if key == 'AuthorisationServers':
                    self._setAuthorisationServers(value)
                else:
                    _mapping[key] = mapping[key]
        self.__dict__.update(_mapping)
        return self

    def serialize(self):
        _mapping = dict()
        for key, value in self.__dict__.items():
            if key in self.__attributes__:
                if key == 'AuthorisationServers':
                    _mapping[key] = [auth.serialize() for auth in value]
                else:
                    _mapping[key] = value
        return _mapping

class ParticipantList:
    __collection__ = 'participants'
    
    def __init__(self):
        self.participants = []
    
    def get_all(self):
        project_list = Participant.__attributes__ + \
            [f'AuthorisationServers.{attr}' for attr in AuthorisationServer.__attributes__]
        project_dict = dict() 
        for project_item in project_list:
            if project_item == '_id':
                project_dict[project_item] = 0
            elif project_item != 'AuthorisationServers':
                project_dict[project_item] = 1
        cursor = app.db[self.__collection__].find({},project_dict)
        self.participants = [Participant().from_mapping(raw) for raw in list(cursor)]
        return self.participants

    def renew(self,data):
        try:
            app.db[self.__collection__].delete_many({})
            app.db[self.__collection__].insert_many(data)
            app.db.upd_history.insert_one({'date':datetime.now()})
        except Exception as e:
            raise Exception("Error while updating database: "+e)
