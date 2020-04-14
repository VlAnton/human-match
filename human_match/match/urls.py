from django.urls import path

from match.views import MatchViewSet


list_view = MatchViewSet.as_view({'get': 'list'})


app_name = 'match'


urlpatterns = [
    path('match/', list_view, name='list')
]
