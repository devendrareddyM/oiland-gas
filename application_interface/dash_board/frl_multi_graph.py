"""Created on Thu Aug  7 15:41:06 2020
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
def frl_multi_line_graph(request):
    if request.method == GET:
        try:
            final_result = []
            # parameter_tag = str(request.GET.get(PARAMETERS))
            Zone = str(request.GET.get('zone'))
            run = str(request.GET.get('run'))
            data = django_search_query(FRL_MULTI_LINE_GRAPH.format(
                Zone=Zone,
                run=run))
            result = data[0]['json_build_object']
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()