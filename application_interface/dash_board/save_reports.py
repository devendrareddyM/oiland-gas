"""
Created on Thu Aug 18 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

# imports
import json
import time as t
import datetime
import jwt
from django.views.decorators.csrf import csrf_exempt

from database.pg_queries import *
from database.pg_query_insert import query_insert_no_role
from database.pg_query_search import django_query_search_no_role_one
from supports.response_module import *
from api_framework.application_config import *
from api_framework.constants import *


# ModifyBuildingDetails
@csrf_exempt
def save_data(request):
    if request.method == POST:
        try:
            request_body = json.loads(request.body)
            sql = []
            import datetime
            ct = datetime.datetime.now()
            for each_one in request_body:
                for each in each_one["Coke Drum"]["actual_values"]:
                    query_now = insert_actual_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Coke Drum"]["predicted_values"]:
                    query_now = insert_predicted_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["input Feed"]["actual_values"]:
                    query_now = insert_actual_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["input Feed"]["predicted_values"]:
                    query_now = insert_predicted_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Heater"]["actual_values"]:
                    query_now = insert_actual_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Heater"]["predicted_values"]:
                    query_now = insert_predicted_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Fractionator"]["actual_values"]:
                    query_now = insert_actual_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Fractionator"]["predicted_values"]:
                    query_now = insert_predicted_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["yields"]["yields_actual_values"]:
                    query_now = insert_actual_data.format(timestamp=request_body[0]['timestamp'],
                                                          parameter=each['parameter'],
                                                          parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                          )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["yields"]["yields_predicted_values"]:
                    query_now = insert_predicted_data.format(timestamp=request_body[0]['timestamp'],
                                                             parameter=each['parameter'],
                                                             parameter_value=each['parameter_value'], unit=each['unit'],current_ts=ct
                                                             )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()

            return response_success(data={
                "message": "Inserted Successfully....."}
            )

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()

    else:
        return response_request_wrong()
