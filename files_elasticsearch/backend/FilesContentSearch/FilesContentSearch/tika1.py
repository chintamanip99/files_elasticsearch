# import tika
# import requests
# from tika import parser
# tika.initVM()
# response = requests.get("https://drive.google.com/file/d/1eWmthQAvpgJdwyJEtcYdyw6X_kdh96ID/view?usp=sharing")
# print(response.content)
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "title contains 'filel' and trashed=false"}).GetList()

for file in file_list:
    print(file['title'], file['id'])
    metadata = dict( id = file['id'] )
    google_file = drive.CreateFile( metadata = metadata )
    google_file.GetContentFile( filename = file['id'] )
    content_bytes = google_file.content
    string_data = content_bytes.read().decode('utf-8')
    print(type(string_data))

# file[0]['id']
# file = drive.CreateFile({'title': 'My Awesome File.txt'})
# file.SetContentString('Hello World!') # this writes a string directly to a file
# file.Upload()