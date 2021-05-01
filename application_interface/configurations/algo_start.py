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
def update_parameter_input_status(request):
    if request.method == PUT:
        try:
            # import datetime
            # s = each['timestamp']
            # fmt = "%Y-%m-%d %H:%M:%S:%S:%Z"
            # t_utc = datetime.datetime.utcfromtimestamp(float(s) / 1000.)
            # t_utc.strftime(fmt)
            query_now = update_parameter_input_status_query
            data = django_query_modify_no_role(sql=query_now)
            if data == 0:
                err = django_query_modify_no_role(sql=query_now)
                return response_conflict(kind='update', err=str(err))

            return response_success(data={
                "message": "Updated Successfully....."}
            )

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()

    else:
        return response_request_wrong()
