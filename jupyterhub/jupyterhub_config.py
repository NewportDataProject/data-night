from oauthenticator.github import LocalGitHubOAuthenticator

server_url = 'https://jupyter.newportdataproject.org'
admins = {'paulopperman', 'davenamin'}
github_clientid = 'GET_FROM_GITHUB'
github_clientsecret = 'GET_FROM_GITHUB'

c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalAuthenticator.create_system_users = True
c.Authenticator.admin_users = admins

c.LocalGitHubOAuthenticator.oauth_callback_url = server_url+'/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = github_clientid
c.LocalGitHubOAuthenticator.client_secret = github_clientsecret
