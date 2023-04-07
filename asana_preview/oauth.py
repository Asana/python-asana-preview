from requests_oauthlib import OAuth2Session

class OAuth(OAuth2Session):
    authorization_base_url = "https://app.asana.com/-/oauth_authorize"
    token_url = "https://app.asana.com/-/oauth_token"
    refresh_url = token_url

    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, **kwargs):
        super(OAuth, self).__init__(**kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
    
    def authorization_url(self):
        return super(OAuth, self).authorization_url(self.authorization_base_url)

    def fetch_token(self, code):
        return super(OAuth, self).fetch_token(self.token_url, client_secret=self.client_secret, code=code)
    
    def refresh_token(self, token):
        extra = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        return super(OAuth, self).fetch_token(self.refresh_url, **extra)
