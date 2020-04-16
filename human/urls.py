from django.urls import path

from human.views import HumanViewSet


app_name = 'human'

list_view = HumanViewSet.as_view({'get': 'list'})
detail_view = HumanViewSet.as_view({'get': 'retreive'})
change_view = HumanViewSet.as_view({'put': 'change'})
delete_view = HumanViewSet.as_view({'delete': 'delete'})
create_view = HumanViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('human/', list_view, name='list'),
    path('human/create', create_view, name='create'),
    path('human/<int:pk>', detail_view, name='detail'),
    path('human/<int:pk>/change', change_view, name='change'),
    path('human/<int:pk>/delete', delete_view, name='delete'),
]