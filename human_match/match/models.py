from django.db import models

from human.models import HumanMixin


class Match(HumanMixin, models.Model):

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
