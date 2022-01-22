import zipfile

path_to_zip_file = "./NATO-alphabet-start.zip"
directory_to_extract_to = "./"
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
