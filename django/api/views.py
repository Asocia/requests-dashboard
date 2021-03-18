from datetime import datetime
from random import random
from time import sleep

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def handle_request(request, format=None):
    """ Return success for all requests """
    sleep_time = random() * 3
    sleep(sleep_time)
    timestamp = int(datetime.now().timestamp())
    log_str = f'{request.method},{sleep_time*1000:.0f},{timestamp}'
    with open('api.log', 'a+') as f:
        print(log_str, file=f)

    return Response(status=status.HTTP_200_OK)


handle_get = api_view(['GET'])(handle_request)
handle_post = api_view(['POST'])(handle_request)
handle_put = api_view(['PUT'])(handle_request)
handle_delete = api_view(['DELETE'])(handle_request)
