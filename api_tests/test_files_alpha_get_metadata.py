"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_metadata
# This will test if the api will retrieve the metadata of a given file.
# Step 1) Create a new file on dropbox. Step 2) call the metadata of
# that file by using the api. Step 3) Assert if the file name created
# matches the metadata file name field.
def test_get_metadata_valid():
    assert True == False