import datetime
import faker
import pytest

from django.conf import settings

from human.models import Human


faker = faker.Faker()


def get_human_data():
    recent_year = datetime.date.today().year
    first_name, second_name = faker.name().split(' ', 1)
    genders = [gender for gender, _ in settings.GENDERS]
    return dict(
        first_name=first_name,
        second_name=second_name,
        age=abs(recent_year - int(faker.year())),
        gender=faker.random.choice(genders)
    )


@pytest.fixture
def humans_env():
    humans = []
    for _ in range(5):
        human_data = get_human_data()
        humans.append(Human(**human_data))
    Human.objects.bulk_create(humans)
