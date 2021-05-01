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
def frl_optimized_ovr_dash(request):
    if request.method == GET:
        try:
            run = str(request.GET.get('run'))
            final_result = []
            data = django_search_query(OPTIMIZED_DATA_SUM_MEAN.format(run=run))
            final_result.append(data)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_request_wrong()
