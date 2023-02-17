from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileStats
from .helpers.helper import FileStatsHelper

import requests
from django.http import JsonResponse


@api_view(['POST'])
def generate_file_stats(request):
    try:
        file_url = request.query_params.get('url')
        if not file_url:
            return JsonResponse({"error": "File url ('url') is required"}, status=400)
        
        file = requests.get(file_url)
        if not file:
            return JsonResponse({"error": "Invalid URL"}, status=400)
        
        # Function to generate the file stats from the file url
        get_stats = FileStatsHelper().process_file_stats(file_url, file)
    
    except Exception as e: 
        return JsonResponse({"error": "Internal Server Error"}, status=500)
    
    return Response(get_stats)


@api_view(['GET'])
def fetch_file_stats(request):
    file_url = request.query_params.get('url')
    if not file_url:
        return JsonResponse({"error": "File url ('url') is required"}, status=400)
    
    try: 
        # Function to fetch the file stats from the file url
        result = FileStats.objects.filter(url= file_url).last()
        response = {
                'Number of Rows': result.num_rows,
                'Number of Columns': result.num_cols,
                'Column wise Distinct value count': result.column_wise_distinct_values, 
                'Column wise Null value count': result.column_wise_null_values
            }
    except Exception: 
        return JsonResponse({"error": "Bad request. Please make sure that you've added the File in the database already"}, status= 400)

    return Response(response)