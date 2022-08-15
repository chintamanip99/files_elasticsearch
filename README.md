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
