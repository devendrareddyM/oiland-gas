"""
Created on Thu Aug  7 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

# imports
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
def over_view_data(request):
    if request.method == GET:
        try:
            # route params data
            final_result = []
            result = {}
            # parameter = str(request.GET.get(PARAMETERS))
            version = str(request.GET.get('version'))
            # if parameter == 'Coke Drum':
            #     a = pd.DataFrame(django_search_query(coke_drum_actual_values))
            #     p = pd.DataFrame(django_search_query(coke_drum_predicted_values.format(version=version)))
            #     y_a = pd.DataFrame(django_search_query(coke_drum_yields_actual_values))
            #     y_p = pd.DataFrame(django_search_query(coke_drum_yields_predicted_values))
            #     if parameter == 'Coke Drum':
            #         result = {
            #             "actual_values": yaml.safe_load(
            #                 a.to_json(orient='records')),
            #             "predicted_values": yaml.safe_load(
            #                 p.to_json(orient='records')),
            #             "yields_actual_values": yaml.safe_load(y_a.to_json(orient='records')),
            #             "yields_predicted_values": yaml.safe_load(
            #                 y_p.to_json(orient='records'))
            #         }
            # if parameter == 'input Feed':
            #     a = pd.DataFrame(django_search_query(feed_actual_values))
            #     p = pd.DataFrame(django_search_query(feed_predicted_values.format(version=version)))
            #     y_a = pd.DataFrame(django_search_query(feed_yields_actual_values))
            #     y_p = pd.DataFrame(django_search_query(feed_yields_predicted_values))
            #     if parameter == 'input Feed':
            #         result = {
            #             "actual_values": yaml.safe_load(
            #                 a.to_json(orient='records')),
            #             "predicted_values": yaml.safe_load(
            #                 p.to_json(orient='records')),
            #             "yields_actual_values": yaml.safe_load(y_a.to_json(orient='records')),
            #             "yields_predicted_values": yaml.safe_load(
            #                 y_p.to_json(orient='records'))
            #         }
            # if parameter == 'Heater':
            #     a = pd.DataFrame(django_search_query(heater_actual_values))
            #     p = pd.DataFrame(django_search_query(heater_predicted_values.format(version=version)))
            #     y_a = pd.DataFrame(django_search_query(heater_yields_actual_values))
            #     y_p = pd.DataFrame(django_search_query(heater_yields_predicted_values))
            #     if parameter == 'Heater':
            #         result = {
            #             "actual_values": yaml.safe_load(
            #                 a.to_json(orient='records')),
            #             "predicted_values": yaml.safe_load(
            #                 p.to_json(orient='records')),
            #             "yields_actual_values": yaml.safe_load(y_a.to_json(orient='records')),
            #             "yields_predicted_values": yaml.safe_load(
            #                 y_p.to_json(orient='records'))
            #         }
            # if parameter == 'Fractionator':
            #     a = pd.DataFrame(django_search_query(fractinator_actual_values))
            #     p = pd.DataFrame(django_search_query(fractinator_predicted_values.format(version=version)))
            #     y_a = pd.DataFrame(django_search_query(fractinator_yields_actual_values))
            #     y_p = pd.DataFrame(django_search_query(fractinator_yields_predicted_values))
            #     if parameter == 'Fractionator':
            #         result = {
            #             "actual_values": yaml.safe_load(
            #                 a.to_json(orient='records')),
            #             "predicted_values": yaml.safe_load(
            #                 p.to_json(orient='records')),
            #             "yields_actual_values": yaml.safe_load(y_a.to_json(orient='records')),
            #             "yields_predicted_values": yaml.safe_load(
            #                 y_p.to_json(orient='records'))
            #         }
            # final_result.append(result)
            # result["Coke Drum"] = {}
            # result["input Feed"] = {}
            # result["Heater"] = {}
            # result["Fractionator"] = {}
            # result["yields"] = {}
            #
            # """ Getting Coke Drum Data """
            # try:
            #     a = pd.DataFrame(django_search_query(coke_drum_actual_values.format(version=version)))
            #     p = pd.DataFrame(django_search_query(coke_drum_predicted_values.format(version=version)))
            #     if not a.empty:
            #         result["Coke Drum"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     else:
            #         result["Coke Drum"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     if not p.empty:
            #         result["Coke Drum"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #     else:
            #         result["Coke Drum"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            # except Exception as err:
            #     return response_exception(err)
            #
            # """ Getting input Feed Data """
            #
            # try:
            #     a = pd.DataFrame(django_search_query(feed_actual_values.format(version=version)))
            #     p = pd.DataFrame(django_search_query(feed_predicted_values.format(version=version)))
            #     if not a.empty:
            #         result["input Feed"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     else:
            #         result["input Feed"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     if not p.empty:
            #         result["input Feed"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #     else:
            #         result["input Feed"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #
            # except Exception as err:
            #     return response_exception(err)
            #
            # """ Getting Heater Data """
            #
            # try:
            #     a = pd.DataFrame(django_search_query(heater_actual_values.format(version=version)))
            #     p = pd.DataFrame(django_search_query(heater_predicted_values.format(version=version)))
            #     if not a.empty:
            #         result["Heater"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     else:
            #         result["Heater"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     if not p.empty:
            #         result["Heater"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #     else:
            #         result["Heater"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #
            # except Exception as err:
            #     return response_exception(err)
            #
            # """ Getting Fractionator Data """
            #
            # try:
            #     a = pd.DataFrame(django_search_query(fractinator_actual_values.format(version=version)))
            #     p = pd.DataFrame(django_search_query(fractinator_predicted_values.format(version=version)))
            #     if not a.empty:
            #         result["Fractionator"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     else:
            #         result["Fractionator"]["actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     if not p.empty:
            #         result["Fractionator"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #     else:
            #         result["Fractionator"]["predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #
            # except Exception as err:
            #     return response_exception(err)
            #
            # """ Getting yields Data """
            #
            # try:
            #     a = pd.DataFrame(django_search_query(dcu_yields_actual_values.format(version=version)))
            #     p = pd.DataFrame(django_search_query(dcu_yields_predicted_values.format(version=version)))
            #     if not a.empty:
            #         result["yields"]["yields_actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     else:
            #         result["yields"]["yields_actual_values"] = yaml.safe_load(
            #             a.to_json(orient='records'))
            #     if not p.empty:
            #         result["yields"]["yields_predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            #     else:
            #         result["yields"]["yields_predicted_values"] = yaml.safe_load(
            #             p.to_json(orient='records'))
            result["Coke Drum"] = {}
            result["input Feed"] = {}
            result["Heater"] = {}
            result["Fractionator"] = {}
            result["yields"] = {}

            """ Getting Coke Drum Data """
            try:
                timestamp = pd.DataFrame(django_search_query("""select max(timestamp) from parameter_input"""))
                if not timestamp.empty:
                    result['timestamp'] = timestamp['max'].iloc[0]
                else:
                    result['timestamp'] = None
                a = pd.DataFrame(django_search_query(coke_actual_values))
                p = pd.DataFrame(django_search_query(coke_predicted_values))
                if not a.empty:
                    result["Coke Drum"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                else:
                    result["Coke Drum"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                if not p.empty:
                    result["Coke Drum"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
                else:
                    result["Coke Drum"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
            except Exception as err:
                return response_exception(err)

            """ Getting input Feed Data """

            try:
                a = pd.DataFrame(django_search_query(input_feed_data))
                p = pd.DataFrame(django_search_query(input_feed_pred_data))
                if not a.empty:
                    result["input Feed"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                else:
                    result["input Feed"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                if not p.empty:
                    result["input Feed"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
                else:
                    result["input Feed"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))

            except Exception as err:
                return response_exception(err)

            """ Getting Heater Data """

            try:
                a = pd.DataFrame(django_search_query(heater_actual_data_values))
                p = pd.DataFrame(django_search_query(heater_pred_data_values))
                if not a.empty:
                    result["Heater"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))

                else:
                    result["Heater"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                if not p.empty:
                    result["Heater"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
                else:
                    result["Heater"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
            except Exception as err:
                return response_exception(err)

            """ Getting Fractionator Data """

            try:
                a = pd.DataFrame(django_search_query(fractinator_actual_data_values))
                p = pd.DataFrame(django_search_query(fractinator_pred_data_values))
                if not a.empty:
                    result["Fractionator"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                else:
                    result["Fractionator"]["actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                if not p.empty:
                    result["Fractionator"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
                else:
                    result["Fractionator"]["predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
            except Exception as err:
                return response_exception(err)

            """ Getting yields Data """

            try:
                a = pd.DataFrame(django_search_query(dcu_yields_actual_data_values))
                p = pd.DataFrame(django_search_query(dcu_yields_result_data))
                if not a.empty:
                    result["yields"]["yields_actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                else:
                    result["yields"]["yields_actual_values"] = yaml.safe_load(
                        a.to_json(orient='records'))
                if not p.empty:
                    result["yields"]["yields_predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))
                else:
                    result["yields"]["yields_predicted_values"] = yaml.safe_load(
                        p.to_json(orient='records'))

            except Exception as err:
                return response_exception(err)

            final_result.append(result)

            return response_success(data=final_result)

        except Exception as err:
            return response_exception(err)
    else:
        return response_request_wrong()
