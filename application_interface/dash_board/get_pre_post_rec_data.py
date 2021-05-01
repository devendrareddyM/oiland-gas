"""
Created on Thu Aug 18 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

# imports
import json
import pandas as pd

import jwt
from django.views.decorators.csrf import csrf_exempt

from database.pg_queries import *
from database.pg_query_modify import django_query_modify_auth, django_query_modify_no_role
from database.pg_query_search import django_search_query
from supports.response_module import *
from api_framework.application_config import *
from api_framework.constants import *


# ModifyBuildingDetails
@csrf_exempt
def get_coke_actual_predicted_post_pre_rec_values(request):
    if request.method == GET:
        try:
            start_date = str(request.GET.get(REQ_START_DATE))
            end_date = str(request.GET.get(REQ_END_DATE))
            parameter = str(request.GET.get(PARAMETERS))
            period = str(request.GET.get('period'))
            final_result = []
            result = {}
            pre_recommended_predicted_data = django_search_query(
                coke_yields_forecast_pre_post_result.format(dw='Pre_Rec',period=period))
            post_recommended_predicted_data = django_search_query(
                coke_yields_forecast_pre_post_result.format(dw='Post_Rec',period=period))
            if parameter == 'pre_rec':
                if not pre_recommended_predicted_data:
                    result["pre_recommended_coke_yields"] = None
                else:
                    result["pre_recommended_coke_yields"] = pre_recommended_predicted_data
            if parameter == 'post_rec':
                if not post_recommended_predicted_data:
                    result["post_recommended_coke_yields"] = None
                else:
                    result["post_recommended_coke_yields"] = post_recommended_predicted_data
            final_result.append(result)
            return response_success(data=final_result)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()

    else:
        return response_request_wrong()
