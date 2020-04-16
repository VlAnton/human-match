import pytest

from django.urls import reverse


pytestmark = pytest.mark.django_db


def test__retreive(client, humans_env):
    human_ids = range(1, 6)
    for human_id in human_ids:
        url = reverse('match:detail', args=[human_id])
        response = client.get(url)
        assert response.status_code == 200


def test__list(client, humans_env):
    url = reverse('match:list')
    response = client.get(url)
    assert response.status_code == 200
