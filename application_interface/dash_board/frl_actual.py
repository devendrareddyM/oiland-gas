"""
Created on Thu feb 22 13:41:06 2021
@author: LIVNSENSE TECHNOLOGIES
Copyright (C) 2021 LivNSense Technologies - All Rights Reserved
"""
# imports
import json
import urllib

import pandas as pd
import jwt
from django.views.decorators.csrf import csrf_exempt
from database.pg_queries import *
from database.pg_query_insert import query_insert_no_role
from database.pg_query_modify import django_query_modify_auth, django_query_modify_no_role
from database.pg_query_search import django_search_query
from supports.response_module import *
from api_framework.application_config import *
from api_framework.constants import *


@csrf_exempt
def get_furnace_run_data(request):
    if request.method == GET:
        try:
            final_result = []
            result = {}
            data = django_search_query(GET_FURNACE_RUN_DATA)
            final_result.append(data)
            import base64
            file = r'C:\Users\nsush\Downloads\Solar\Solar\Solar\Sample failed module images\DJI_0804.jpg'
            image = open(file, 'rb')
            image_read = image.read()
            result = base64.b64encode(image_read)
            data = urllib.parse.quote(result)
            # sql = []
            # image = data
            # over = 'yes'
            # query_now = vision_insert.format(image=image, over=over
            #                                  )
            # sql.append(query_now)
            # query_insert_no_role(sql=sql)
            # sql.pop()
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_request_wrong()
