"""
Created on Thu Aug  7 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

# imports
import json
import numpy as np

import pandas as pd
import jwt
import yaml
from django.views.decorators.csrf import csrf_exempt

from api_framework.application_config import *
from api_framework.constants import *
from database.pg_queries import *
from database.pg_query_search import *


# Get_admin_User_Details
@csrf_exempt
def get_start_and_end_data(request):
    if request.method == GET:
        try:
            final_result = []
            result = {}
            st_end_dt = django_search_query(actual_predicted_st_end_date)
            result["actual"] = st_end_dt[0]['json_build_object']
            result["fore_cast"] = st_end_dt[1]['json_build_object']
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
