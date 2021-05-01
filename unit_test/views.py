from django.shortcuts import render

# Create your views here.
import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from psycopg2.extras import RealDictCursor
from database.pg_conn import pg_connection
from database.pg_queries import *
from api_framework.application_config import *
from supports.status import *
from api_framework.settings import DATABASES
import json
from api_framework.constants import *

# AddDriverDetails
@csrf_exempt
def delete_test(request):
    if request.method == 'POST':
        jwt_token = request.headers.get(AUTHORIZATION, None)
        if jwt_token is not None:
            try:
                token = jwt_token.split(' ')
                payload = jwt.decode(token[TOKEN_SLICED_LOCATION], JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])

                user_id = payload['user_id']
                request_body = json.loads(request.body)
                role_id = payload[REQ_ROLE_ID]
                conn = pg_connection(DATABASES)
                if role_id == 1 or role_id == 2:
                    if conn:
                        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                            pass

                            # Creating new user id
                            # cursor.execute(test_case_delete_query.format(request_body['vehicle_reg'],
                            #                                              request_body['license_number'],
                            #                                              request_body['user_name']
                            #                                              ))
                            # data = cursor.fetchone()
                            # try:
                            #     # Delete Queries
                            #     cursor.execute(delete_user_details_query.format(data['user_id']))
                            #     cursor.execute(delete_user_master_query.format(data['user_id']))
                            #     conn.commit()
                            #
                            # except Exception as err:
                            #     return JsonResponse({'message': 'Unable to insert due to ' + str(err) + ''},
                            #                         safe=False,
                            #                         status=HTTP_409_CONFLICT)

                            return JsonResponse({"message": "Deleted Successfully....."},
                                                safe=False,
                                                status=HTTP_200_OK)
                    else:
                        return JsonResponse({'message': 'No Data Base Connection'},
                                            safe=False,
                                            status=HTTP_501_NOT_IMPLEMENTED)
                else:
                    return JsonResponse({'message': 'UnAuthorised User'},
                                        safe=False,
                                        status=HTTP_401_UNAUTHORIZED)

            except Exception as err:
                return JsonResponse({'message': str(err)}, safe=False, status=HTTP_404_NOT_FOUND)
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return JsonResponse({'message': 'Token is invalid'},
                                    safe=False,
                                    status=HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({'message': 'No Token'},
                                safe=False,
                                status=HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse({'message': 'Wrong Request Error'},
                            safe=False,
                            status=HTTP_400_BAD_REQUEST)
