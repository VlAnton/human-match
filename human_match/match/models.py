from django.db import models


SEXES = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
)


class Match(models.Model):

    first_name = models.CharField('First name', max_length=50, blank=False)
    second_name = models.CharField('Second name', max_length=50, blank=False)
    age = models.PositiveIntegerField('Age', blank=False)
    gender = models.CharField('Gender', max_length=10, blank=False, choices=SEXES)

    class Meta:
        db_table = 'match'
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def jsonify(self):
        return self.__class__.objects.filter(id=self.id).values().first()