# Objective - Test if the api can upload a file to DB.
# Expected Outcome - The file can be seen on DB.
def test_upload_validation():
    assert True == False

# Objective - Input an acceptable upload path to upload a file to DB.
# Expected Outcome - if upload path is acceptable, uploaded file will
# be on DB.
def test_upload_path():
    assert True == False

# Objective - Input an unacceptable upload path on DB (use incorrect
# formats, ie. use '\' instead of '/')
# Expected Outcome - should receive an error when curling, which should
# prevent file from uploading.
def test_upload_path_invalid():
    assert True == False

# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:add when uploading.
# Expected Outcome - Existing file should not be overwritten, instead
# the same file name should exist with an appended '#'. Ex:
# "Document(2).txt"
def test_upload_mode_add():
    assert True == False

# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:upload when uploading.
# Expected Outcome - File uploaded will overwrite the existing file. Name
# will be the same.
def test_upload_mode_override():
    assert True == False

# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:update when uploading.
# Expected Outcome - File will overwrite if the rev is the same. The
# autorename will add string "conflicted copy" to the file.
def test_upload_mode_update():
    assert True == False

# Objective - Test to see what makes the upload mode invalid. Ex: Leave
# the field blank when uploading (not sure this is right).
# Expected Outcome - This will default to the "add" option, which will
# not overwrite the file, but will create another file and append a #
# to it.
def test_upload_mode_invalid():
    assert True == False

# Objective - Test to see if DB will autorename the file if there is a
# conflict with the mode.
# Expected Outcome - File will be autorenamed by DB.
def test_upload_autorename_false()
    assert True == False

# Objective - Test to see if DB will autorename the file if there is a
# conflict with the mode.
# Expected Outcome - File will be autorenamed by DB.
def test_upload_authorname_true():
    assert True == False

# Objective - See if inputting a timestamp when a user uploads the file
# will appear on the "client modified" response.
# Expected Outcome - Time stamp appears exactly what was inputted by the
# user under "client modified" response.
def test_upload_client_modified_future():
    assert True == False

@pytest.mark.mute
# Objective - Upload the file with mute: True.
# Expected Outcome - User should not receive a notification on this
# modification.
def test_upload_mute_true():
    assert True == False

@pytest.mark.mute
# Objective - Upload the file with mute: False.
# Expected Outcome - User should receive a notification on any
# modification to the file.
def test_upload_mute_false():
    assert True == False

# Objective - Test to see if original uploaded file size is the same as
# the size response.
# Expected Outcome - Size reponse and original uploaded file size are
# equal.
def test_upload_response_size():
    assert True == False

# Objective - Check to see if the response for pathlower starts with a '/'
# Expected Outcome - Response field pathlower will start with '/'.
def test_upload_response_pathlower():
    assert True == False

# Objective - Create an error that returns a malformed response.
# Expected Outcome - Receive a malformed response error message that
# could not save the file.
def test_upload_error_malformed_path():
    assert True == False

# Objective - Create a situation that does not give the user permission
# to write to the target location.
# Expected Outcome - User receives an error and cannot write the file to
# the target location.
def test_upload_error_no_write_permission():
    assert True == False

# Objective - Create a situation where the user goes over the available
# space (bytes) when uploading a file.
# Expected Outcome - User received an error that they cannot write the
# file to target location due to insufficient space
def test_upload_error_insufficient_space():
    assert True == False

# Objective - Upload a file or folder with an inappropriate name or name
# format.
# Expected Outcome - Receive an error that the file cannot be saved due
# to the file or folder name.
def test_upload_error_disallowed_name():
    assert True == False