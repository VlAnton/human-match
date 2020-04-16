from django.urls import path, include

from human import urls as human_urls
from match import urls as match_urls

urlpatterns = [
    path('', include(human_urls)),
    path('', include(match_urls)),
]
