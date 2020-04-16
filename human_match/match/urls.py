from django.urls import path

from match.views import MatchViewSet


list_view = MatchViewSet.as_view({'get': 'list'})
detail_view = MatchViewSet.as_view({'get': 'retreive'})


app_name = 'match'


urlpatterns = [
    path('match/', list_view, name='list'),
    path('match/<int:human_pk>', detail_view, name='detail'),
]
