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
def add_predicted_config_values(request):
    if request.method == POST:
        try:
            # parameter = str(request.GET.get(PARAMETERS))
            parameter = None
            request_body = json.loads(request.body)
            table = None
            equipment_id = None
            process_id = None
            sql = []
            if parameter == "Coke Drum":
                table = 'plant_coke_drum'
                process_id = 1
                equipment_id = 1
            if parameter == 'Fractionator':
                table = 'plant_fractinator'
                process_id = 4
                equipment_id = 4
            if parameter == 'input Feed':
                table = 'plant_feed_data'
                process_id = 2
                equipment_id = 2
            if parameter == 'Heater':
                table = 'plant_heater'
                process_id = 3
                equipment_id = 3
            timestamp = (datetime.datetime.now()).strftime(
                UTC_DATE_TIME_FORMAT)
            get_last_coke_id = django_query_search_no_role_one(
                sql=get_version_number.format(table_name='plant_coke_drum'))
            if get_last_coke_id['max'] is None:
                new_coke_id = 1
            else:
                new_coke_id = get_last_coke_id['max'] + 1
            get_last_feed_id = django_query_search_no_role_one(
                sql=get_version_number.format(table_name='plant_feed_data'))
            if get_last_feed_id['max'] is None:
                new_feed_id = 1
            else:
                new_feed_id = get_last_feed_id['max'] + 1
            get_last_heater_id = django_query_search_no_role_one(
                sql=get_version_number.format(table_name='plant_heater'))
            if get_last_heater_id['max'] is None:
                new_heater_id = 1
            else:
                new_heater_id = get_last_heater_id['max'] + 1
            get_last_fractionator_id = django_query_search_no_role_one(
                sql=get_version_number.format(table_name='plant_fractinator'))
            if get_last_fractionator_id['max'] is None:
                new_fractionator_id = 1
            else:
                new_fractionator_id = get_last_fractionator_id['max'] + 1
            get_last_yields_id = django_query_search_no_role_one(
                sql=get_version_number.format(table_name='dcu_yields'))
            if get_last_yields_id['max'] is None:
                new_yields_id = 1
            else:
                new_yields_id = get_last_yields_id['max'] + 1
            for each_one in request_body:
                for each in each_one["Coke Drum"]["actual_values"]:
                    table = 'plant_coke_drum'
                    process_id = 1
                    equipment_id = 1
                    query_now = insert_actual_values.format(table_name=table, equipment_id=equipment_id,
                                                            process_id=process_id,
                                                            parameter=each['parameter'], max_value=each['max_value'],
                                                            min_value=each['min_value'], timestamp=timestamp,
                                                            uom=each['uom'], version=new_coke_id,
                                                            process_value=each['process_value']
                                                            )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Coke Drum"]["predicted_values"]:
                    table = 'plant_coke_drum'
                    process_id = 1
                    equipment_id = 1
                    query_now = insert_predicted_values.format(table_name=table, equipment_id=equipment_id,
                                                               process_id=process_id,
                                                               parameter=each['parameter'], max_value=each['max_value'],
                                                               min_value=each['min_value'], timestamp=timestamp,
                                                               uom=each['uom'], version=new_coke_id,
                                                               )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["input Feed"]["actual_values"]:
                    table = 'plant_feed_data'
                    process_id = 2
                    equipment_id = 2
                    query_now = insert_actual_values.format(table_name=table, equipment_id=equipment_id,
                                                            process_id=process_id,
                                                            parameter=each['parameter'], max_value=each['max_value'],
                                                            min_value=each['min_value'], timestamp=timestamp,
                                                            uom=each['uom'], version=new_feed_id,
                                                            process_value=each['process_value']
                                                            )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["input Feed"]["predicted_values"]:
                    table = 'plant_feed_data'
                    process_id = 2
                    equipment_id = 2
                    query_now = insert_predicted_values.format(table_name=table, equipment_id=equipment_id,
                                                               process_id=process_id,
                                                               parameter=each['parameter'], max_value=each['max_value'],
                                                               min_value=each['min_value'], timestamp=timestamp,
                                                               uom=each['uom'], version=new_feed_id,
                                                               )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Heater"]["actual_values"]:
                    table = 'plant_heater'
                    process_id = 3
                    equipment_id = 3
                    query_now = insert_actual_values.format(table_name=table, equipment_id=equipment_id,
                                                            process_id=process_id,
                                                            parameter=each['parameter'], max_value=each['max_value'],
                                                            min_value=each['min_value'], timestamp=timestamp,
                                                            uom=each['uom'], version=new_heater_id,
                                                            process_value=each['process_value']
                                                            )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Heater"]["predicted_values"]:
                    table = 'plant_heater'
                    process_id = 3
                    equipment_id = 3
                    query_now = insert_predicted_values.format(table_name=table, equipment_id=equipment_id,
                                                               process_id=process_id,
                                                               parameter=each['parameter'], max_value=each['max_value'],
                                                               min_value=each['min_value'], timestamp=timestamp,
                                                               uom=each['uom'], version=new_heater_id,
                                                               )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Fractionator"]["actual_values"]:
                    table = 'plant_fractinator'
                    process_id = 4
                    equipment_id = 4
                    query_now = insert_actual_values.format(table_name=table, equipment_id=equipment_id,
                                                            process_id=process_id,
                                                            parameter=each['parameter'], max_value=each['max_value'],
                                                            min_value=each['min_value'], timestamp=timestamp,
                                                            uom=each['uom'], version=new_fractionator_id,
                                                            process_value=each['process_value']
                                                            )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["Fractionator"]["predicted_values"]:
                    table = 'plant_fractinator'
                    process_id = 4
                    equipment_id = 4
                    query_now = insert_predicted_values.format(table_name=table, equipment_id=equipment_id,
                                                               process_id=process_id,
                                                               parameter=each['parameter'], max_value=each['max_value'],
                                                               min_value=each['min_value'], timestamp=timestamp,
                                                               uom=each['uom'], version=new_fractionator_id,
                                                               )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["yields"]["yields_actual_values"]:
                    table = 'dcu_yields'
                    process_id = 1
                    equipment_id = 1
                    query_now = insert_actual_values.format(table_name=table, equipment_id=equipment_id,
                                                            process_id=process_id,
                                                            parameter=each['parameter'], max_value=each['max_value'],
                                                            min_value=each['min_value'], timestamp=timestamp,
                                                            uom=each['uom'], version=new_yields_id,
                                                            process_value=each['process_value']
                                                            )
                    sql.append(query_now)
                    query_insert_no_role(sql=sql)
                    sql.pop()
                for each in each_one["yields"]["yields_predicted_values"]:
                    table = 'dcu_yields'
                    process_id = 1
                    equipment_id = 1
                    query_now = insert_predicted_values.format(table_name=table, equipment_id=equipment_id,
                                                               process_id=process_id,
                                                               parameter=each['parameter'], max_value=each['max_value'],
                                                               min_value=each['min_value'], timestamp=timestamp,
                                                               uom=each['uom'], version=new_yields_id,
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
