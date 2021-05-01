# imports
import jwt
from django.views.decorators.csrf import csrf_exempt

from api_framework.constants import *
from database.pg_queries import *
from database.pg_query_search import django_search_query
from supports.response_module import *


@csrf_exempt
def get_cpr_sor_eor(request):
    if request.method == GET:
        try:
            final_result = []
            run = str(request.GET.get('run'))
            sor_eor = str(request.GET.get('param'))
            data = django_search_query(CPR_SOR_EOR.format(min_max=sor_eor, run=run))
            data = data[0]['json_build_object']
            final_result.append(data)
            return response_success(data=final_result)
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_request_wrong()
