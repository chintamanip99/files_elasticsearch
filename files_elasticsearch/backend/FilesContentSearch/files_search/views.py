from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework import serializers
from django.utils.timezone import now,localtime
import datetime
import random
from django.core.mail import send_mail,BadHeaderError
from rest_framework import generics
from rest_framework import filters
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from django_dbq.models import Job
from common.elasticsearch_config import connection

@api_view(['GET'])
def run_jobs(request):
    Job.objects.create(name="my_job")
    return Response({"job":"enqeued"})

@api_view(['GET'])
def index_files(request):
    if request.method=='GET':
        Job.objects.create(name="index_files_job")
        return Response({"job":"enqeued"})

@api_view(['GET'])
def google_drive_callback(request):
    print(request,"this is the request")
    return Response({'auth':'done'})

@api_view(['GET'])
def search(request):
    response = connection.search(
        index="my_files",
        body={
            "query": {
                "bool": {
                "must": [{"match": {"data":request.GET.get('q','any text here')}}],
                }
            },
            "aggs" : {
                "per_tag": {
                "terms": {"field": "tags"},
                    "aggs": {
                        "max_lines": {"max": {"field": "lines"}}
                    }
                }
            }

        }
    )
    files = []
    for hit in response['hits']['hits']:
        files.append({ "file_name" : hit['_source']['file_name'], "url" : hit['_source']['url'] })
    return Response({"files" : files})