class AuthorisationServer:
    __attributes__ = ['CustomerFriendlyName','CustomerFriendlyLogoUri','OpenIDDiscoveryDocument'] 
    
    def __init__(self):
        self.CustomerFriendlyName = ""
        self.CustomerFriendlyLogoUri = ""
        self.OpenIDDiscoveryDocument = ""
    
    def from_mapping(self, mapping = dict()):
        _mapping = dict()
        for key, value in mapping.items():
            if hasattr(self, key):
                _mapping[key] = value
        self.__dict__.update(_mapping)

    def serialize(self):
        _mapping = dict()
        for key, value in self.__dict__.items():
            if key in self.__attributes__:
                _mapping[key] = value
        return _mapping