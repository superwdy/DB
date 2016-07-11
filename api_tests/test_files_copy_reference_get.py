"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_copy
# This will test if the api will provide a copy reference code for other
# users to copy files to their dropbox account. Step 1) Create any file
# on dropbox. Step 2) Use the copy ref api. Step 3) Assert if the json
# returned a copy ref code (check to see the ref code field is not blank).
def test_copy_ref():
    assert True == False