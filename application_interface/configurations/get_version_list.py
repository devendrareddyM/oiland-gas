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
def get_version_list(request):
    if request.method == GET:
        try:
            parameter = str(request.GET.get(PARAMETERS))
            table_name=None
            if parameter == "Coke Drum":
                table_name = 'plant_coke_drum'
            if parameter == 'Fractionator':
                table_name = 'plant_fractinator'
            if parameter == 'input Feed':
                table_name = 'plant_feed_data'
            if parameter == 'Heater':
                table_name = 'plant_heater'
            data = pd.DataFrame(
                django_search_query(get_predicted_version_list.format(table_name=table_name)))
            if not data.empty:
                data = list(data['version'])
            else:
                data = data.to_json(orient="records")
                data = json.loads(data)
            return response_success(data=data)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()

    else:
        return response_request_wrong()
