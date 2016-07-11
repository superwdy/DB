
"""
Code	Description
400	Bad input parameter. Error message should indicate which one and why.
401	Bad or expired token. This can happen if the user or Dropbox revoked or expired an access token. To fix, you should re-authenticate the user.
403	Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won't help here.
404	File or folder not found at the specified path.
405	Request method not expected (generally should be GET or POST).
429	Your app is making too many requests and is being rate limited. 429s can trigger on a per-app or per-user basis.
503	If the response includes the Retry-After header, this means your OAuth 1.0 app is being rate limited. Otherwise, this indicates a transient server error, and your app should retry its request.
507	User is over Dropbox storage quota.
5xx	Server error. Check DropboxOps.
"""
hostname = ['api.dropboxapi.com', 'content.dropboxapi.com','notify.dropboxapi.com']
response_type = ''
client_id = ''