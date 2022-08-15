# files_elasticsearch
Elastic searching ability to search files over google drive. 

I have created an application which can be used to search the files on the basis of their content.
At frontend : React Js
At backend : Python-Django , ElasticSearch engine.

1) I have taken an input string from web app and passed to the backend of the application.
2) Then the backend returns the response containing the file names and their google drive urls respectively.
3) For creating indexes of the files is to call an api which will trigger a job at backend.
4) The job running at backend lists all the files on my google drive's searchable_files folder and the corresponding indexes for the files are created   iteratively for each file in bulk.
5) We will have our searable indices stored in elastic search engine by using which we can search the files on the basis of their content.

Settingup the frontend:
1) Download the frontend project
2) run : npm install
3) run : npm start
4) Hurray! the frontend app started!

Settingup the ELasticSearch engine:
1) Download latest version of elastic search
2) Unzip the .tar file
3) Navigate into the extracted folder 
4) run : bin/elasticsearch
5) Yes! elastic search engine is now ready to receive the requests.

Settingup the backend:
1) Download the backend project 
2) run : pip install -r requirements.txt
3) run : python manage.py makemigrations
4) run : python manage.py runserver
5) Hurray! the backend of the app also started.
