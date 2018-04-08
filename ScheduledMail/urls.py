from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^details/(?P<id>\w{0,50})/$', views.details),
    path("compose", views.compose, name='compose')
]

