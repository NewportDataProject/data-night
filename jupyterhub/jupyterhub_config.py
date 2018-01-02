from oauthenticator.github import LocalGitHubOAuthenticator
from .secrets.py import GITHUB_APP_ID, GITHUB_APP_SECRET

server_url = 'http://jupyter.newportdataproject.org'
admins = {'paulopperman', 'davenamin'}
github_clientid = GITHUB_APP_ID
github_clientsecret = GITHUB_APP_SECRET

c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalAuthenticator.create_system_users = True
c.Authenticator.admin_users = admins

c.LocalGitHubOAuthenticator.oauth_callback_url = server_url+'/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = github_clientid
c.LocalGitHubOAuthenticator.client_secret = github_clientsecret
