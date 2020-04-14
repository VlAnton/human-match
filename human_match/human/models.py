from django.db import models

from match.models import Match


class Human(Match):

    avatar = models.ImageField('Avatar', null=True)

    class Meta:
        db_table = 'human'
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'
