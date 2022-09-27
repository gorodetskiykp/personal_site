from collections import defaultdict
from http import HTTPStatus
import requests
from requests.exceptions import ConnectionError
from django.http import JsonResponse
from django.shortcuts import render

from .models import Video
from core.services import check_resource


def index(request):
    videos = Video.objects.all()
    template = 'videos/index.html'
    videos_dict = defaultdict(list)
    for video in videos:
        video_item = {}
        video_item['link'] = video.link
        video_item['link_status'] = video.link
        video_item['title'] = video.title
        video_item['description'] = video.description
        video_item['language'] = video.language
        video_item['difficult'] = video.difficult
        if video.author_github_link:
            video_item['author_github_link'] = video.author_github_link
        if video.my_github_link:
            video_item['my_github_link'] = video.my_github_link
        for category in video.categories.all():
            videos_dict[category.title].append(video_item)
    context = {
        'videos': dict(videos_dict),
    }
    return render(request, template, context)


def check_resource(request):
    link = request.GET.get('link', None)
    print(link)

    try:
        net_response = requests.get(link)
        result = net_response.status_code == HTTPStatus.OK
    except ConnectionError:
        result = False
    # print(net_response.status_code)
    response = {
        'availability': result
    }
    return JsonResponse(response)
