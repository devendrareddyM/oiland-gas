from django.http import JsonResponse
from supports.status import *
from supports.logger_file import *


def response_exception(err):
    logger.error({'message': str(err)})
    return JsonResponse({'message': str(err)},
                        safe=False,
                        status=HTTP_403_FORBIDDEN)


def response_nodbconn():
    logger.error({'message': 'No Data Base Connection'})
    return JsonResponse({'message': 'No Data Base Connection'},
                        safe=False,
                        status=HTTP_503_SERVICE_UNAVAILABLE)


def response_unauthorised():
    logger.error({'message': 'unauthorized user'})
    return JsonResponse({'message': 'unauthorized'},
                        safe=False,
                        status=HTTP_403_FORBIDDEN)


def response_request_wrong():
    logger.error({'message': 'Wrong Request Error'})
    return JsonResponse({'message': 'Wrong Request Error'},
                        safe=False,
                        status=HTTP_400_BAD_REQUEST)


def response_invalid_token():
    logger.error({'message': 'Token is invalid'})
    return JsonResponse({'message': 'Token is invalid'},
                        safe=False,
                        status=HTTP_401_UNAUTHORIZED)


def exception_err(err):
    logger.error({'message': str(errors=err)})


def response_success(data):
    return JsonResponse(data=data,
                        safe=False,
                        status=HTTP_200_OK)


def response_conflict(kind, err):
    return JsonResponse(
        {
            'message': 'Unable to {kind} due to  {err}'.format(kind=str(kind), err=str(err))
        },
        safe=False,
        status=HTTP_409_CONFLICT)
