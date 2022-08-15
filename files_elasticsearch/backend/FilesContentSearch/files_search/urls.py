from django.urls import path,include
from .views import index_files, google_drive_callback, search, run_jobs

app_name="files_search_engine"

urlpatterns = [
	path('index_files',index_files,name='files_search_name'),
    path('search',search,name='search'),
    path('gdcallback',google_drive_callback,name='google_drive_callback'),
    path('run_jobs',run_jobs,name='run_jobs'),
]