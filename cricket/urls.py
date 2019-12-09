from .views import *
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^get_team_1/$', views.getTeam1),
    re_path(r'^get_team_2/$', views.getTeam2),
    re_path(r'^get_match_date/$', views.getMatchDate),
    re_path(r'^get_data/$', views.getData),
]