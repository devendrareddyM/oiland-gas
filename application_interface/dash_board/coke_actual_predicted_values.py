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
def get_coke_actual_predicted_values(request):
    if request.method == GET:
        try:
            final_result = []
            result = {}
            actual_data = django_search_query(coke_yields_actual_values)
            pre_recommended_predicted_data = django_search_query(coke_yields_forecast_result.format(dw='Pre_Rec'))
            post_recommended_predicted_data = django_search_query(coke_yields_post_rec_forecast_values.format(dw='Post_Rec'))
            weekly_forecast_pre_data = django_search_query(weekly_coke_yields_forecast_result.format(dw='Pre_Rec'))
            weekly_forecast_post_data = django_search_query(weekly_coke_yields_post_rec_forecast_result.format(dw='Post_Rec'))
            if not actual_data:
                result["coke_yields"] = None
            else:
                result["coke_yields"] = actual_data[0]['coke_yields']
            if not pre_recommended_predicted_data:
                result["current_pre_recommended_coke_yields"] = None
            else:
                result["current_pre_recommended_coke_yields"] = pre_recommended_predicted_data[0]['pre_recommended_coke_yields']
            if not post_recommended_predicted_data:
                result["current_post_recommended_coke_yields"] = None
            else:
                result["current_post_recommended_coke_yields"] = post_recommended_predicted_data[0][
                    'pre_recommended_coke_yields']
            if not weekly_forecast_pre_data:
                result["weekly_pre_recommended_coke_yields"] = None
            else:
                result["weekly_pre_recommended_coke_yields"] = weekly_forecast_pre_data[0]['pre_recommended_coke_yields']
            if not weekly_forecast_post_data:
                result["weekly_post_recommended_coke_yields"] = None
            else:
                result["weekly_post_recommended_coke_yields"] = weekly_forecast_post_data[0][
                    'pre_recommended_coke_yields']
            final_result.append(result)
            return response_success(data=final_result)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()

    else:
        return response_request_wrong()
