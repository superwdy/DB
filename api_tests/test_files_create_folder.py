"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_folder
# This will test if the api can create a folder. Step 1) Create the
# folder using the create_folder api. Step 2) Assert if the folder
# exists by searching for it using the search API
def test_create_folder():
    assert True == False

@pytest.mark.files_folder
# This will test if the api can accept a folder with different formats.
# Step 1) Create a list of names that include strings, integers, and
# special chars. Step 2) Use the create folder api and run a for loop
# to iterate through each format. Step 3) Assert that after each run
# the status code response == 200.
def test_create_folder_format():
    assert True == False