import os
import asana_preview
import json
from flask import Flask, request, session, redirect, render_template_string
from asana_preview.api import users_api

# OAuth Instructions:
#
# 1. create a new application in your Asana Account Settings ("App" panel)
# 2. set the redirect URL to "http://localhost:5000/auth/asana/callback" (or whichever port you choose)
# 3. set your ASANA_CLIENT_ID and ASANA_CLIENT_SECRET environment variables

# convience method to create a client with your credentials, and optionally a 'token'
def Client(**kwargs):
    return asana_preview.Client.oauth(
        client_id=os.environ["ASANA_CLIENT_ID"],
        client_secret=os.environ["ASANA_CLIENT_SECRET"],
        redirect_uri="http://localhost:5000/auth/asana/callback",
        **kwargs
    )

app = Flask(__name__)

@app.route("/")
def main():
    token = session.get("token", False)
    # if the user has a token they're logged in
    if token:
        # example request gets information about logged in user
        api_client = Client(token=token)
        api_instance = users_api.UsersApi(api_client)
        me = api_instance.get_user("me")["data"]
        return render_template_string(
            """
<script>
    window.opener.postMessage("success", "https://app.asana.com");
</script>
<p>Hello {{ name }}.</p>
<p><pre>{{ dump }}</pre></p>
<p><a href="/logout">Logout</a></p>""",
            name=me["name"],
            dump=json.dumps(me.to_dict(), indent=2),
        )
    # if we don't have a token show a "Sign in with Asana" button
    else:
        # get an authorization URL and anti-forgery "state" token
        (auth_url, state) = Client().authorization_url()
        # persist the state token in the user's session
        session["state"] = state
        # link the button to the authorization URL
        return render_template_string(
            """
<p><a href="{{ auth_url }}"><img src="https://luna1.co/7df202.png"></a></p>""",
            auth_url=auth_url,
        )


# logout endpoint
@app.route("/logout")
def logout():
    # delete the session token and redirect back to the main page
    del session["token"]
    return redirect("/")


# OAuth callback endpoint
@app.route("/auth/asana/callback")
def auth_callback():
    session["token"] = Client().fetch_token(code=request.args.get("code"))
    return redirect("/")


app.secret_key = "set this to something secret"

if __name__ == "__main__":
    app.run(debug=True)
