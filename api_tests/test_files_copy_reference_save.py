"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_copy
# This will test if the api can use a ref code to copy an existing file
# to users dropbox account. Step 1) Create any file on dropbox. Step 2)
# Use the copy ref api and save the copy ref data. Step 3) Use the copy
# ref save api with the ref from the previous step. Step 4) Assert the
# created file from step 1 matches the copied file from step 3.
def test_copy_ref_save():
    assert True == False