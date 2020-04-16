from django.conf import settings
from django.db import models

from common.managers import RandomManager
from common.mixins import JsonMixin


class Match(JsonMixin, models.Model):
    first_name = models.CharField('First name', max_length=50, blank=False)
    second_name = models.CharField('Second name', max_length=50, blank=False)
    age = models.PositiveIntegerField('Age', blank=False)
    gender = models.CharField('Gender', max_length=10, blank=False, choices=settings.GENDERS)

    objects = RandomManager()

    class Meta:
        db_table = 'match'
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
