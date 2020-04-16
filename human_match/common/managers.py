import random

from django.db import models


class RandomManager(models.Manager):
    def random(self):
        """Возвращает рандомную запись."""
        return random.choice(self.all())
