import pytest

from django.urls import reverse

from conftest import get_human_data
from human.models import Human


pytestmark = pytest.mark.django_db


class TestHumanViewSet:
    def test__create(self, client):
        assert Human.objects.count() == 0

        url = reverse('human:create')
        post_data = get_human_data()

        response = client.post(url, post_data)
        assert response
        assert Human.objects.count() == 1
