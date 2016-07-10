"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_copy
# This will test if the api will copy an existing file on dropbox to a
# new path. Step 1) Create any file on dropbox. Step 2) Use the
# copy api to copy the file onto a different path. Step 3) Assert if
# the file name matches the metadata name by using the search API.
def test_copy_valid():
    assert True == False

@pytest.mark.files_copy
# This will test if the api will copy an existing file on dropbox to an
# existing path. Step 1) Create any file on dropbox. Step 2) Create a
# new directory. Step 3) Use the copy api to copy the file onto the new
# created path. Step 4) Assert if the file name and path matches the
# metadata name and path by using the search API.
def test_copy_existing_path():
    assert True == False

