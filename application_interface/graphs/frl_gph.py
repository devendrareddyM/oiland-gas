
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
def dash_board_frl_graph(request):
    if request.method == GET:
        try:
            final_result = []
            parameter_tag = str(request.GET.get(PARAMETERS))
            Zone = str(request.GET.get('zone'))
            run = str(request.GET.get('run'))
            data = django_search_query(FRL_GRAPH.format(
                parameter_tag=parameter_tag,
                Zone=Zone,
                run=run))
            result = data[0]['json_build_object']
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()