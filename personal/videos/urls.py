from django.urls import path
from . import views


app_name = 'videos'
urlpatterns = [
    path('', views.index, name='index'),
    path('check_resource/', views.check_resource, name='check_resource'),

]
