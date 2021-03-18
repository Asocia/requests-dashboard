
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def handle_request(request, format=None):
    """ Return success for all requests """

    return Response(status=status.HTTP_200_OK)


handle_get = api_view(['GET'])(handle_request)
handle_post = api_view(['POST'])(handle_request)
handle_put = api_view(['PUT'])(handle_request)
handle_delete = api_view(['DELETE'])(handle_request)
