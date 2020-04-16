from rest_framework import serializers

from match.models import Match
from human.models import Human


class MatchSerializer(serializers.ModelSerializer):
    human = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ('__all__')

    def get_human(self, obj) -> 'dict':
        """Возвращает данные о рандомном пользователе."""
        return Human.objects.random().jsonify()
