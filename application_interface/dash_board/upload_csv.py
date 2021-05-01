"""
Created on Thu Aug 18 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

# imports
import io
import os

import jwt
import pandas
from django.views.decorators.csrf import csrf_exempt
from psycopg2._psycopg import cursor
from api_framework.application_config import *
from api_framework.constants import *
from database.pg_queries import *
from database.pg_query_insert import django_query_insert_csv, django_query_insert_specific_role, query_insert_no_role
from database.pg_query_search import django_search_query
from supports.response_module import *


# ModifyBuildingDetails
@csrf_exempt
def upload_details(request):
    if request.method == POST:
        try:
            file = request.FILES.getlist('files')
            for file in file:
                extension = os.path.splitext(file.name)[1]
                from database.pg_conn import pg_connection
                from django.db import connection as conn
                if extension == ".csv":
                    sql1 = []
                    file_data = pandas.read_csv(file, encoding='ISO-8859-1')
                    employee_data = file_data
                    # credential_data = file_data[['employee_id', 'role', 'password']]
                    # emp_cols = ','.join(list(employee_data.columns))
                    # with open(file_data, 'r') as f:
                    #     print(f)
                    # employee_data.to_csv('upload.csv', index_label='id', header=False, index=False)
                    # f = open('upload.csv', 'r')
                    # try:
                    #     cursor = conn.cursor()
                    #     cursor.copy_from(f, 'raw_data', sep=",")
                    #     conn.commit()
                    # except Exception as err:
                    #     return JsonResponse(
                    #         {
                    #             'message': 'Unable to insert   {err}'.format(err=str(err))
                    #         },
                    #         safe=False,
                    #         status=HTTP_409_CONFLICT)

                    for index, row in employee_data.iterrows():
                        query_one = UPLOAD_RAW_DATA.format(obs_time=row['obs_time'],
                                                           run=row['run'],
                                                           runlength=row['runlength'],
                                                           efrz1=row['efrz1'], efrz2=row['efrz2'], efrz3=row['efrz3'],
                                                           dsfz1=row['dsfz1'], dsfz2=row['dsfz2'], dsf3=row['dsf3'],
                                                           shcrz1=row['shcrz1'], shcrz2=row['shcrz2'],
                                                           shcrz3=row['shcrz3'],
                                                           cotp3=row['cotp3'], cotp1=row['cotp1'], cotp6=row['cotp6'],
                                                           cotp5=row['cotp5'],
                                                           cptp2=row['cptp2'], cotp4=row['cotp4'], cotz1=row['cotz1'],
                                                           cotz2=row['cotz2'], cotz3=row['cotz3'],
                                                           cprz1=row['cprz1'], cprz2=row['cprz2'], cprz3=row['cprz3'],
                                                           tmtz1=row['tmtz1'], tmtz2=row['tmtz2'], tmtz3=row['tmtz3'],
                                                           ptle_temp=row['ptle_temp'], stle_temp=row['stle_temp'],
                                                           fgffz1=row['fgffz1'], ffwz1=row['ffwz1'],
                                                           fgffz2=row['fgffz2'],
                                                           ffwz2=row['ffwz2'], fgffz3=row['fgffz3'], ffwz3=row['ffwz3'],
                                                           fgpfz1=row['fgpfz1'], fgpwz1=row['fgpwz1'],
                                                           fgpfz2=row['fgpfz2'], fgpwz2=row['fgpwz2'],
                                                           fgpfz3=row['fgpfz3'], fgpwz3=row['fgpwz3'], bwt=row['bwt'],
                                                           ofg=row['ofg'], fd=row['fd'], shst=row['shst'],
                                                           shsp=row['shsp'], dosage=row['dosage'],
                                                           es=row['es'], cpr_z1_c1=row['cpr_z1_c1'],
                                                           cpr_z1_c2=row['cpr_z1_c2'], cpr_z1_c3=row['cpr_z1_c3'],
                                                           cpr_z1_c4=row['cpr_z1_c4'], cpr_z1_c5=row['cpr_z1_c5'],
                                                           cpr_z1_c6=row['cpr_z1_c6'], cpr_z1_c7=row['cpr_z1_c7'],
                                                           cpr_z1_c8=row['cpr_z1_c8'], cpr_z2_c1=row['cpr_z2_c1'],
                                                           cprz2_c2=row['cprz2_c2'], cprz2_c3=row['cprz2_c3'],
                                                           cprz2_c4=row['cprz2_c4'], cprz2_c5=row['cprz2_c5'],
                                                           cprz2_c6=row['cprz2_c6'], cprz2_c7=row['cprz2_c7'],
                                                           cprz2_c8=row['cprz2_c8'], cprz3_c1=row['cprz3_c1'],
                                                           cprz3_c2=row['cprz3_c2'], cprz3_c3=row['cprz3_c3'],
                                                           cprz3_c4=row['cprz3_c4'], cprz3_c5=row['cprz3_c5'],
                                                           cprz3_c6=row['cprz3_c6'], cprz3_c7=row['cprz3_c7'],
                                                           cprz3_c8=row['cprz3_c8'], max_cpr=row['max_cpr']

                                                           )
                        sql1.append(query_one)
                        try:
                            data, err = query_insert_no_role(sql=sql1)
                            sql1.pop(0)
                            if err:
                                return JsonResponse(
                                    {
                                        'message': 'Unable to insert   {err}'.format(err=str(err))
                                    },
                                    safe=False,
                                    status=HTTP_409_CONFLICT)

                        except:
                            sql1.pop(0)
            return response_success({
                "message": "Inserted Successfully....."})
        except Exception as err:
            return response_exception(err)
    else:
        return response_invalid_token()
