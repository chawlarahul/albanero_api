from django.db import models

# Create your models here.

import logging
logger = logging.getLogger(__name__)

class FileStats(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    url = models.CharField(max_length=1000)
    num_rows = models.IntegerField(blank=True)
    num_cols = models.IntegerField(blank=True)
    column_wise_distinct_values = models.JSONField(default=dict, blank=True)
    column_wise_null_values = models.JSONField(default=dict, blank=True)