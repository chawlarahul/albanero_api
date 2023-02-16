from django import views
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from core.models import *
from rest_framework.exceptions import NotFound
# from pyspark.sql import SparkSession

import logging
logger = logging.getLogger(__name__)


class ProcessFileViewset(viewsets.ViewSet):
    @action(methods=["get"], detail=False, url_path=r"upload_file_stats")
    def process_file_stats(self, request):
        pass

    @action(methods=["get"], detail=False, url_path=r"fetch_file_stats")
    def fetch_file_stats(self, request):
        pass