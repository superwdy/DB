"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.auth
# Test if this api will disable the access token used to authenticate
# the call. After the api is executed, run a get request from any api
# and use the recently disabled token to see if it is still valid.
# Assert status code != 200.
def test_auth_token_revoke():
    assert True == False