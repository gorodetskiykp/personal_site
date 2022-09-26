from django.shortcuts import render
from collections import defaultdict
from .models import Video


def index(request):
    videos = Video.objects.all()
    template = 'videos/index.html'
    videos_dict = defaultdict(list)
    for video in videos:
        video_item = {}
        video_item['link'] = video.link
        video_item['title'] = video.title
        video_item['description'] = video.description
        video_item['language'] = video.language
        video_item['difficult'] = video.difficult
        video_item['author_github_link'] = video.author_github_link
        video_item['my_github_link'] = video.my_github_link
        for category in video.categories.all():
            videos_dict[category.title].append(video_item)
    context = {
        'videos': dict(videos_dict),
    }
    return render(request, template, context)
