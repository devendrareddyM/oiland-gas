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
def pie_chart_data(request):
    if request.method == GET:
        try:
            final_result = []
            result = {}
            actual_values_data = django_search_query(pie_dcu_actual_yields)
            predicted_values_data = django_search_query(pie_dcu_predicted_yields)
            recommended_values_data = django_search_query(pie_dcu_recommended_yields)
            recommended_other_yields_data = django_search_query(pie_dcu_recommended_other_yields)
            result["actual_yields_data"] = actual_values_data
            result["predicted_yields_data"] = predicted_values_data
            result["recommended_yields_data"] = recommended_values_data
            result["recommended_other_yields_data"] = recommended_other_yields_data
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
