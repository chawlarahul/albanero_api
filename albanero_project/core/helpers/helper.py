import json
import logging
from django.conf import settings
from django.http import JsonResponse

import pandas as pd
import io

from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct, isnull, sum

from core.models import FileStats

logger = logging.getLogger(__name__)


class FileStatsHelper:
    def __init__(self):
        self.spark = SparkSession.builder.appName("FileStats").getOrCreate()

    def process_file_stats(self,file_url, file):
        try:
            spark = self.spark

            data = io.StringIO(file.text)
            pd_df = pd.read_csv(data, sep=",")
            df = spark.createDataFrame(pd_df)
            
            # Generate file stats using PySpark
            # Get "number of rows" and "number of columns"
            num_rows = df.count() 
            num_cols = len(df.columns) 

            # Get "Column wise Distinct value count " and "Column wise Distinct value count"
            columns = df.columns
            
            distinct_counts = [df.agg(countDistinct(column)).collect()[0][0] for column in columns]
            null_counts = [df.where(isnull(column)).count() for column in columns]

            distinct_count_output = {}
            null_count_output = {}

            for i, column in enumerate(columns):
                distinct_count_output[column]=distinct_counts[i]
                null_count_output[column]=null_counts[i]


            # Store file stats in the database
            FileStats.objects.get_or_create(
                url=file_url, 
                num_rows=num_rows, 
                num_cols=num_cols, 
                column_wise_distinct_values= distinct_count_output, 
                column_wise_null_values= null_count_output
            )
            
            # Return file stats as JSON response
            response = {
                'Number of Rows': num_rows,
                'Number of Columns': num_cols,
                'Column wise Distinct value count': distinct_count_output, 
                'Column wise Null value count': null_count_output
            }
        except Exception as e:
            raise e
        return response
    