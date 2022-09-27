import requests
from http import HTTPStatus
from django.http import JsonResponse


def check_resource(request):
    link = request.GET.get('link', None)
    net_response = requests.get(link)
    response = {
        'availability': net_response.status_code == HTTPStatus.OK
    }
    return JsonResponse(response)

