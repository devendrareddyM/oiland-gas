### Zone Wise information
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

@csrf_exempt
def get_zone_wise_data(request):
    if request.method == GET:
        try:
            final_result = []
            result = {}
            data = django_search_query(GET_ZONE_WISE_DATA)

            final_result.append(data)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_request_wrong()