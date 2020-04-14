from rest_framework import status, permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from human.models import Human, Match
from match.serializers import MatchSerializer


class MatchViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = MatchSerializer

    def list(self, request):
        serializer = self.serializer_class(instance=Match.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
