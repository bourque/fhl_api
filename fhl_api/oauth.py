"""
"""

from yahoo_oauth import OAuth2

def authorize():
    """
    """

    oauth = OAuth2(None, None, from_file='oauth.json')
    if not oauth.token_is_valid():
        oauth.refresh_access_token()

    return oauth

SESSION = authorize()