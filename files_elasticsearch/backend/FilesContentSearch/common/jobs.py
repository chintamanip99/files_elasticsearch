from time import sleep
from common.elasticsearch_config import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
import json

gauth = GoogleAuth()

def my_task(job):
    print("Working hard...")
    sleep(10)
    print("Job\'s done!")

def yield_docs():
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    folders_list = drive.ListFile({'q': "mimeType='application/vnd.google-apps.folder'"}).GetList()
    folder_id = ''
    for folder in folders_list:
            print(folder['title'], folder['id'])
            if(folder['title']=='searchable_files'):
                folder_id = folder['id']
                print(folder_id)
                break
    qeury_str = "'"+folder_id+"' in parents and trashed=false"
    file_list = drive.ListFile({'q': qeury_str}).GetList()
    id=0
    print("File indexing started")
    for file in file_list:
        print("Indexing the file : "+file['title']+", id : "+ file['id'])
        metadata = dict( id = file['id'] )
        google_file = drive.CreateFile( metadata = metadata )
        # access_token = gauth.credentials.access_token
        # file_id = google_file['id']
        # url = 'https://www.googleapis.com/drive/v3/files/' + file_id + '/permissions?supportsAllDrives=true'
        # headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
        # payload = {'type': 'anyone', 'value': 'anyone', 'role': 'reader'}
        # res = requests.post(url, data=json.dumps(payload), headers=headers)
        # print("res is ",res.body)
        google_file.GetContentFile( filename = file['id'] )
        content_bytes = google_file.content
        string_data = content_bytes.read().decode('utf-8')
        doc_source = {
            "file_name": file['title'],
            "url" : google_file['alternateLink'],
            "data": string_data
            }
        yield {
            "_index": "my_files",
             "_id": id + 1,
             "_source": doc_source
            }
        id+=1
    print("File indexing ended")

def index_searchable_files(job):
    try:
        resp = helpers.bulk(
            connection,
            yield_docs()
            )
        print("Successfully indexed")
    except Exception as err:
        print("\nindexing error: helpers.bulk() ERROR:", err)