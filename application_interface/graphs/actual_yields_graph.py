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
def actual_yields_graph_data(request):
    if request.method == GET:
        try:
            # route params data
            final_result = []
            result = {}
            start_date = str(request.GET.get(REQ_START_DATE))
            end_date = str(request.GET.get(REQ_END_DATE))
            sfbl = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Sweet_FG_to_Battery_limit', st_date=start_date,
                                                           end_date=end_date))
            lpg = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Sweet_LPG', st_date=start_date,
                                                           end_date=end_date))
            lcn = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Total_LCN', st_date=start_date,
                                                           end_date=end_date))
            hcn = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Total_HCN', st_date=start_date,
                                                           end_date=end_date))
            lcgo = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Total_LCGO', st_date=start_date,
                                                           end_date=end_date))
            hcgo = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Total_HCGO', st_date=start_date,
                                                           end_date=end_date))
            coke = django_search_query(
                actual_yields_graph_data_in_percent.format(parameter='Coke', st_date=start_date, end_date=end_date))
            result['Sweet_FG_to_Battery_limit'] = sfbl
            result['Sweet_LPG'] = lpg
            result['LCN'] = lcn
            result['HCN'] = hcn
            result['LCGO'] = lcgo
            result['HCGO'] = hcgo
            result['Coke'] = coke

            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
