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
def dash_board_frl_optimised_multi_line_graph(request):
    if request.method == GET:
        try:
            final_result = []
            Zone = str(request.GET.get('zone'))
            run = str(request.GET.get('run'))
            Ethane = None
            SHC = None
            cot = None
            if Zone == 'Zone 1':
                Ethane = 'efrz1'
                SHC = 'shcrz1'
                cot = 'cot1'
            if Zone == 'Zone 2':
                Ethane = 'efrz2'
                SHC = 'shcrz2'
                cot = 'cot2'
            if Zone == 'Zone 3':
                Ethane = 'efrz2'
                SHC = 'shcrz2'
                cot = 'cot3'
            if Zone == 'Zone 4':
                Ethane = 'efrz4'
                SHC = 'shcrz4'
                cot = 'cot4'

            data = django_search_query(OPTIMISED_MULTI_LINE_GRAPH.format(
                Ethane=Ethane,
                SHC=SHC,
                cot=cot,
                run=run))
            result = data[0]['json_build_object']
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
