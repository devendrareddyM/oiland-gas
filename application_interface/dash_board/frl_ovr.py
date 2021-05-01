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
def frl_ovr_view_dash(request):
    if request.method == GET:
        try:
            run = str(request.GET.get('run'))
            param = str(request.GET.get('param'))
            final_result = []
            if param == '0':
                data = django_search_query(FRL_OVR_DATA.format(run=run))
                data = data[0]['json_build_object']
                final_result.append(data)
            else:
                run = django_search_query(MAX_RUN)
                data = django_search_query(FRL_OVR_DATA.format(run=run[0]['max']))
                data = data[0]['json_build_object']
                final_result.append(data)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_request_wrong()
