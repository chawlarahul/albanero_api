from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileStats
from .helpers.helper import FileStatsHelper

import requests
from django.http import JsonResponse


# Create your views here.
@api_view(['POST'])
def file_stats(request):
    try:
        file_url = request.query_params.get('url')
        file = requests.get(file_url)
        if not file:
            return JsonResponse({"error": "Invalid URL"}, status=400)
        get_stats = FileStatsHelper().process_file_stats(file_url, file)
        return Response(get_stats)
    except Exception as e: 
        # logger.error(str(e))
        return Exception("Invalid url")
    
    # except Exception as e:
    #     return Response(f"Received error in views.file_stats {e}")
        