"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_upload
# This will test if the api will upload a .txt file. Step 1) Create a
# new .txt file on your desktop. 2) Upload the file. 3) Assert if the
# file name matches the metadata name by using the search API.
def test_upload_file_txt():
    assert True == False

@pytest.mark.files_upload
# This will test if api will upload a .jpg file. Step 1) Create a new
# .jpg file on your desktop. 2) Upload the file. 3) Assert if the file
# matches the metadata file name by using the search API.
def test_upload_file_jpg():
    assert True == False

@pytest.mark.files_upload
# This will test if api will upload a .mpg file. Step 1) Create a new
# .mpg file on your desktop. 2) Upload the file. 3) Assert if the file
# matches the metadata file name by using the search API.
def test_upload_file_mpg():
    assert True == False

@pytest.mark.files_upload
# This will test if the api will upload a file with a different
# extension from the created file. Step 1) Create any new file on your
# desktop. Step 2) Upload the file, but change the extension of the
# file name on the path field so it does NOT match the new file
# extention Ex: created file extension is .txt, but the path created is
# .mpg. 3) Assert if the file can be uploaded with different extensions
# by seeing if the status code == 200. Can run a further test if the
# file can be "played" (I know it will error out).
def test_upload_file_path_different():
    assert True == False

