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
def dash_board_frl_optimised_graph(request):
    if request.method == GET:
        try:
            final_result = []
            parameter_tag = str(request.GET.get(PARAMETERS))
            Zone = str(request.GET.get('zone'))
            run = str(request.GET.get('run'))
            print(parameter_tag)
            column = None
            uom = None
            if parameter_tag == 'Ethane Feed' and Zone == 'Zone 1':
                column = 'efrz1'
                uom = 'kg/hr'
            if parameter_tag == 'Ethane Feed' and Zone == 'Zone 2':
                column = 'efrz2'
                uom = 'Kg/hr'
            if parameter_tag == 'Ethane Feed' and Zone == 'Zone 3':
                column = 'efrz3'
                uom = 'Kg/hr'
            if parameter_tag == 'Ethane Feed' and Zone == 'Zone 4':
                column = 'efrz4'
                uom = 'Kg/hr'
            if parameter_tag == 'SHC Ratio' and Zone == 'Zone 1':
                column = 'shcrz1'
                uom = '%'
            if parameter_tag == 'SHC Ratio' and Zone == 'Zone 2':
                column = 'shcrz2'
                uom = '%'
            if parameter_tag == 'SHC Ratio' and Zone == 'Zone 3':
                column = 'shcrz3'
                uom = '%'
            if parameter_tag == 'SHC Ratio' and Zone == 'Zone 4':
                column = 'shcrz4'
                uom = '%'
            if parameter_tag == 'COT' and Zone == 'Zone 1':
                column = 'cot1'
                uom = '°C'
            if parameter_tag == 'COT' and Zone == 'Zone 2':
                column = 'cot2'
                uom = '°C'
            if parameter_tag == 'COT' and Zone == 'Zone 3':
                column = 'cot3'
                uom = '°C'
            if parameter_tag == 'COT' and Zone == 'Zone 4':
                column = 'cot4'
                uom = '°C'

            data = django_search_query(OPTIMISED_GRAPH__DATA.format(
                param_name=parameter_tag,
                column=column,
                uom=uom,
                run=run))
            result = data[0]['json_build_object']
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
