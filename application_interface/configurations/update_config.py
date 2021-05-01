"""
Created on Thu Aug 18 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

# imports
import json

import jwt
from django.views.decorators.csrf import csrf_exempt

from database.pg_queries import *
from database.pg_query_modify import django_query_modify_auth, django_query_modify_no_role
from supports.response_module import *
from api_framework.application_config import *
from api_framework.constants import *


# ModifyBuildingDetails
@csrf_exempt
def update_predicted_config_values(request):
    if request.method == PUT:
        try:
            parameter = str(request.GET.get(PARAMETERS))
            request_body = json.loads(request.body)
            predicted_table = None
            if parameter == "Coke Drum":
                predicted_table = 'plant_coke_drum'
            if parameter == 'Fractionator':
                predicted_table = 'plant_fractinator'
            if parameter == 'input Feed':
                predicted_table = 'plant_feed_data'
            if parameter == 'Heater':
                predicted_table = 'plant_heater'
            for each in request_body:
                # import datetime
                #
                # s = each['timestamp']
                # fmt = "%Y-%m-%d %H:%M:%S:%S:%Z"
                # t_utc = datetime.datetime.utcfromtimestamp(float(s) / 1000.)
                # t_utc.strftime(fmt)
                query_now = update_config_predict_values.format(table_name=predicted_table, min_value=each['min_value'],
                                                                max_value=each['max_value'], parameter=each['parameter'],version=each['version']
                                                                )
                django_query_modify_no_role(sql=query_now)
                # if data == 0:
                #      return response_conflict(kind='update', err=str(err))

            return response_success(data={
                "message": "Updated Successfully....."}
            )

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()

    else:
        return response_request_wrong()
