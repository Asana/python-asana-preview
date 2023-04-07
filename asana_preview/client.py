from asana.api_client import ApiClient
from asana.configuration import Configuration
from asana.oauth import OAuth

class Client(object):

    def __init__(self):
        pass

    def access_token(access_token, **kwargs):
        configuration = Configuration(access_token=access_token, **kwargs)
        return ApiClient(configuration)

    def oauth(**kwargs):
       if 'token' in kwargs:
            configuration = Configuration(access_token=kwargs.get("token")["access_token"])
            return ApiClient(configuration)
       return OAuth(**kwargs)
