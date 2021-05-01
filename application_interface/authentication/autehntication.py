"""
Created on Thu Aug  7 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description: It authenticates the user to login. On successful login it provides token.

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""
import json

import jwt
from django.views.decorators.csrf import csrf_exempt

from api_framework.application_config import *
from api_framework.constants import *
from database.pg_queries import *
from database.pg_query_search import *
from supports.response_module import *


def jwt_creation(data):
    return {"token": str(jwt.encode(data,
                                    JWT_SECRET,
                                    algorithm=JWT_ALGORITHM
                                    ))
            }


@csrf_exempt
def authentication(request):
    try:
        if request.method == POST:
            try:
                request_body = json.loads(request.body)

                sql = login_query.format(
                    email_id=request_body['email_id'],
                    password=request_body['password'])

                record = django_search_query(sql=sql)
                if len(record) > 0:
                    rec = {
                        "user_id": record[0][DB_EMAIL_ID],
                        "first_name": record[0][DB_COL_F_NAME],
                        "role": record[0][DB_COL_ROLE_TYPE]

                    }
                    return response_success(data=jwt_creation(rec))

                else:
                    return response_unauthorised()

            except Exception as err:
                return response_exception(err)
        else:
            return response_request_wrong()
    except Exception as err:
        return response_exception(err)
