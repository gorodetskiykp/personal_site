from django.contrib import admin

from .models import Category, Video, Link

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Link)
