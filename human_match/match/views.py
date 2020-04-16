import datetime
from faker import Faker

from django.conf import settings

from rest_framework import status, permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from human.models import Human
from match.models import Match
from match.serializers import MatchSerializer


class MatchViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = MatchSerializer

    @property
    def existing_match(self) -> 'match.Match' or None:
        """
        Возвращает произвольный объект Match, если количество Human не больше количества Match.
        """
        if Match.objects.count() >= Human.objects.count():
            return Match.objects.random()

    @property
    def new_match(self) -> 'match.Match':
        """Создаёт и возвращает новый объект Match."""
        faker = Faker()
        recent_year = datetime.date.today().year
        first_name, second_name = faker.name().split(' ', 1)
        genders = [gender for gender, _ in settings.GENDERS]
        match_data = {
            'first_name': first_name,
            'second_name': second_name,
            'age': abs(recent_year - int(faker.year())),
            'gender': faker.random.choice(genders)
        }
        return Match.objects.create(**match_data)

    def list(self, request):
        serializer = self.serializer_class(instance=Match.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retreive(self, request, human_pk):
        try:
            human = Human.objects.get(pk=human_pk)
        except Human.DoesNotExist as ex:
            return Response(data={'error': str(ex)}, status=status.HTTP_404_NOT_FOUND)
        else:
            match = self.existing_match
            if match is None:
                match = self.new_match
            data = match.jsonify()
            data['human'] = human.jsonify()
            return Response(data, status=status.HTTP_200_OK)
