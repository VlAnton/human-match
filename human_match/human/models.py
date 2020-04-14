from django.db import models


class HumanMixin:
    """"""

    SEXES = (
        ('Man', 'Man'),
        ('Woman', 'Woman'),
    )
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=SEXES)


class Human(HumanMixin, models.Model):
    """"""

    avatar = models.ImageField('Avatar')

    class Meta:
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'
