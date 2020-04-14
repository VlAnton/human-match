from rest_framework import serializers

from human.models import Human, Match


class MatchSerializer(serializers.ModelSerializer):

    human = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ('__all__')
        exlude = ('id')

    def get_human(self, obj):
        return Human.objects.get(id=obj.id).jsonify()
