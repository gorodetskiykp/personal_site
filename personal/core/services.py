import requests
from http import HTTPStatus


def check_resourse(link):
    response = requests.get(link)
    return response.status_code == HTTPStatus.OK

