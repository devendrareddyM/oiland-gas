"""
Created on Thu Aug  7 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

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
def dash_board_graph(request):
    if request.method == GET:
        try:
            # route params data
            final_result = []
            result = {}
            res = pd.DataFrame()
            # parameter = str(request.GET.get('module'))
            parameter_tag = str(request.GET.get(PARAMETERS))
            start_date = str(request.GET.get(REQ_START_DATE))
            end_date = str(request.GET.get(REQ_END_DATE))
            period = str(request.GET.get('period'))
            # if parameter == 'Coke Drum':
            #     y_a = pd.DataFrame(
            #         django_search_query(coke_drum_yields_actual_values_graph.format(parameter=parameter_tag,
            #                                                                         start_date=start_date,
            #                                                                         end_date=end_date)))
            #     y_p = pd.DataFrame(
            #         django_search_query(coke_drum_yields_predicted_values_graph.format(parameter=parameter_tag,
            #                                                                            start_date=start_date,
            #                                                                            end_date=end_date)))
            #     if not y_a.empty and not y_p.empty:
            #         res = pd.merge(y_a, y_p, on='timestamp')
            #         # result = {
            #         #     "yields_actual_values": list(y_a['process_value']),
            #         #     "yields_predicted_values": list(y_p['process_value']),
            #         #     "x-axis": list(y_a['timestamp']),
            #         #     "unit": y_a['uom'][0]
            #         # }
            # if parameter == 'input Feed':
            #     y_a = pd.DataFrame(
            #         django_search_query(feed_yields_actual_values_graph.format(parameter=parameter_tag,
            #                                                                    start_date=start_date,
            #                                                                    end_date=end_date)))
            #     y_p = pd.DataFrame(
            #         django_search_query(feed_yields_predicted_values_graph.format(parameter=parameter_tag,
            #                                                                       start_date=start_date,
            #                                                                       end_date=end_date)))
            #     if not y_a.empty and not y_p.empty:
            #         res = pd.merge(y_a, y_p, on='timestamp')
            #         # result = {
            #         #     "yields_actual_values": list(y_a['process_value']),
            #         #     "yields_predicted_values": list(y_p['process_value']),
            #         #     "x-axis": list(y_a['timestamp']),
            #         #     "unit": y_a['uom'][0]
            #         # }
            # if parameter == 'Heater':
            #     y_a = pd.DataFrame(
            #         django_search_query(heater_yields_actual_values_graph.format(parameter=parameter_tag,
            #                                                                      start_date=start_date,
            #                                                                      end_date=end_date)))
            #     y_p = pd.DataFrame(
            #         django_search_query(heater_yields_predicted_values_graph.format(parameter=parameter_tag,
            #                                                                         start_date=start_date,
            #                                                                         end_date=end_date)))
            #     if not y_a.empty and not y_p.empty:
            #         res = pd.merge(y_a, y_p, on='timestamp')
            #         # result = {
            #         #     "yields_actual_values": list(y_a['process_value']),
            #         #     "yields_predicted_values": list(y_p['process_value']),
            #         #     "x-axis": list(y_a['timestamp']),
            #         #     "unit": y_a['uom'][0]
            #         # }
            # if parameter == 'Fractionator':
            #     y_a = pd.DataFrame(
            #         django_search_query(fractinator_yields_actual_values_graph.format(parameter=parameter_tag,
            #                                                                           start_date=start_date,
            #                                                                           end_date=end_date)))
            #     y_p = pd.DataFrame(
            #         django_search_query(fractinator_yields_predicted_values_graph.format(parameter=parameter_tag,
            #                                                                              start_date=start_date,
            #                                                                              end_date=end_date)))
            if parameter_tag != 'coke_yields' and parameter_tag != 'predicted':
                # print(parameter_tag)
                # act_parameter = parameter_tag
                # pred_parameter = parameter_tag
                # if parameter_tag == 'LCN':
                #     act_parameter = 'Total_LCN'
                #     pred_parameter = parameter_tag
                # elif parameter_tag == 'HCN':
                #     act_parameter = 'Total_HCN'
                #     pred_parameter = parameter_tag
                # elif parameter_tag == 'LCGO':
                #     act_parameter = 'Total_LCGO'
                #     pred_parameter = parameter_tag
                # elif parameter_tag == 'HCGO':
                #     act_parameter = 'Total_HCGO'
                #     pred_parameter = parameter_tag
                # elif parameter_tag == 'Sweet_LPG':
                #     act_parameter = 'Sweet_LPG'
                #     pred_parameter = parameter_tag
                # elif parameter_tag == 'Sweet_FG_to_Battery_limit':
                #     act_parameter = 'Sweet_FG_to_Battery_limit'
                #     pred_parameter = parameter_tag
                # elif parameter_tag == 'Sweet_LPG':
                #     act_parameter = parameter_tag
                #     pred_parameter = 'Sweet_LPG'
                # elif parameter_tag == 'Sweet_FG_to_Battery_limit':
                #     act_parameter = parameter_tag
                #     pred_parameter = 'Sweet_FG_to_Battery_limit'
                # elif parameter_tag == 'Total_HCGO':
                #     act_parameter = parameter_tag
                #     pred_parameter = 'HCGO'
                # elif parameter_tag == 'Total_LCGO':
                #     act_parameter = parameter_tag
                #     pred_parameter = 'LCGO'
                # elif parameter_tag == 'Total_HCN':
                #     act_parameter = parameter_tag
                #     pred_parameter = 'HCN'
                # elif parameter_tag == 'Total_LCN':
                #     act_parameter = parameter_tag
                #     pred_parameter = 'LCN'
                y_a = pd.DataFrame(
                    django_search_query(dcu_yields_actual_values_graph.format(parameter=parameter_tag,
                                                                              start_date=start_date,
                                                                              end_date=end_date)))
                y_p = pd.DataFrame(
                    django_search_query(dcu_yields_predicted_values_graph.format(parameter=parameter_tag
                                                                                 )))
                if not y_a.empty:
                    result['actual_values'] = yaml.safe_load(
                        y_a.to_json(orient="records"))
                else:
                    result['actual_values'] = []

                if not y_p.empty:
                    result['recommended_values'] = float(y_p.predicted_value.iloc[0])
                else:
                    result['recommended_values'] = None
                # if not y_a.empty and not y_p.empty:
                #     res = pd.merge(y_a, y_p, on='timestamp')
                #     if parameter_tag in ['LCN', 'HCN', 'LCGO', 'HCGO', 'Sweet_LPG', 'Sweet_FG_to_Battery_limit',
                #                          'Total_HCGO', 'Total_LCGO', 'Total_LCN', 'Total_HCN']:
                #         res.drop(columns=['parameter_x', 'parameter_y'], inplace=True)
                #     # result = {
                #     #     "yields_actual_values": list(y_a['process_value']),
                #     #     "yields_predicted_values": list(y_p['process_value']),
                #     #     "x-axis": list(y_a['timestamp']),
                #     #     "unit": y_a['uom'][0]
                #     # }
                # if not y_a.empty and y_p.empty:
                #     y_p = pd.DataFrame({
                #         'parameter': parameter_tag, 'predicted_value': np.NaN}, index=[0])
                #     res = pd.merge(y_a, y_p, on='parameter')
                #     if parameter_tag in ['LCN', 'HCN', 'LCGO', 'HCGO', 'Sweet_LPG', 'Sweet_FG_to_Battery_limit',
                #                          'Total_HCGO', 'Total_LCGO', 'Total_LCN', 'Total_HCN']:
                #         res.drop(columns=['parameter_x', 'parameter_y'], inplace=True)
                #     else:
                #         res.drop(columns=['parameter'], inplace=True)
                # if not y_p.empty and y_a.empty:
                #     y_a = pd.DataFrame({
                #         'parameter': parameter_tag, 'actual_value': np.NaN}, index=[0])
                #     res = pd.merge(y_a, y_p, on='parameter')
                #     if parameter_tag in ['LCN', 'HCN', 'LCGO', 'HCGO', 'Sweet_LPG', 'Sweet_FG_to_Battery_limit',
                #                          'Total_HCGO', 'Total_LCGO', 'Total_LCN', 'Total_HCN']:
                #         res.drop(columns=['parameter_x', 'parameter_y'], inplace=True)
                #     else:
                #         res.drop(columns=['parameter'], inplace=True)
            if parameter_tag == "coke_yields":
                y_a = pd.DataFrame(
                    django_search_query(dcu_yields_actual_values_graph.format(parameter='Coke',
                                                                              start_date=start_date,
                                                                              end_date=end_date)))
                y_p = pd.DataFrame(
                    django_search_query(dcu_yields_predicted_values_graph.format(parameter='Coke'
                                                                                 )))
                if not y_a.empty:
                    result['actual_values'] = yaml.safe_load(
                        y_a.to_json(orient="records"))
                else:
                    result['actual_values'] = []

                if not y_p.empty:
                    result['recommended_values'] = float(y_p.predicted_value.iloc[0])
                else:
                    result['recommended_values'] = None
            if parameter_tag == 'predicted' and start_date == '' and end_date == '' and period:
                data = django_search_query(predicted_parameters_graph_data.format(
                    dw='Pre_Rec',
                    period=period))
                post_rec = django_search_query(predicted_parameters_graph_data.format(
                    dw='Post_Rec',
                    period=period))

                if not data:
                    result['pre_fore_cast_data'] = None
                else:
                    result['pre_fore_cast_data'] = data[0]['json_build_object']
                if not post_rec:
                    result["post_fore_cast_data"] = None
                else:
                    result["post_fore_cast_data"] = post_rec[0]['json_build_object']
            final_result.append(result)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
