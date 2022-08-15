from elasticsearch import Elasticsearch, helpers
connection = Elasticsearch(['https://filescontentsearch.es.us-east-2.aws.elastic-cloud.com/'],cloud_id="FilesContentSearch:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbSQ3MDA4YzBkMzQwZTY0YTMxYTMxNGY4OTdkNmE1OWM3NCQyOGM2NTc3YjZkNjc0MjAzOTllOTRhZmExYjEwN2VkMg==",basic_auth=("elastic", "ThsfoSfxTnrzytmd71FylVzr"),ssl_assert_fingerprint="315F161C7F7D61FD263680005EB4FC0148EAADED")

def yield_docs():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': "title contains 'filel' and trashed=false"}).GetList()
    id=0
    for file in file_list:
        print(file['title'], file['id'])
        metadata = dict( id = file['id'] )
        google_file = drive.CreateFile( metadata = metadata )
        google_file.GetContentFile( filename = file['id'] )
        content_bytes = google_file.content
        string_data = content_bytes.read().decode('latin-1')
        doc_source = {
            "file_name": file['title'],
            "data": string_data
            }
            # use a yield generator so that the doc data isn't loaded into memory
        yield {
            "_index": "my_files",
            "_type": "text",
             "_id": id + 1, # number _id for each iteration
             "_source": doc_source
            }
        id+=1