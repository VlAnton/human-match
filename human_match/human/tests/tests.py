import pytest
import json

from django.urls import reverse

from conftest import get_human_data
from human.models import Human


pytestmark = pytest.mark.django_db


class TestHumanViewSet:
    """Набор тестов для HumanViewSet."""

    def get_humans_from_response(self, content):
        content = content.decode()
        return json.loads(content)

    def test__create(self, apiclient):
        """
        :Действие: создание объекта Human с помощью метода HumanViewSet.create

        :Ожидаемый результат: статус ответа == 200, человек успешно создан
        """
        assert Human.objects.count() == 0

        url = reverse('human:create')
        post_data = get_human_data()

        response = apiclient.post(url, post_data)
        assert response.status_code == 200
        assert Human.objects.count() == 1

    def test__list(self, apiclient, humans):
        """
        :Окружение: набор объектов Human
        :Действие: получение списка Human с помощью метода HumanViewSet.create

        :Ожидаемый результат: статус ответа == 200, человек успешно создан,
                            исходный набор Human соответствует полученному
        """
        url = reverse('human:list')

        response = apiclient.get(url)
        response_content = response.getvalue()
        assert response.status_code == 200

        received_humans = self.get_humans_from_response(response_content)
        expected_humans = list(humans.values())

        sort_by_id_key = lambda d: d['id']
        received_humans.sort(key=sort_by_id_key)
        expected_humans.sort(key=sort_by_id_key)
        assert received_humans == expected_humans

    def test__change(self, apiclient, humans):
        """
        :Окружение: набор объектов Human
        :Действие: изменение объекта Human с помощью метода HumanViewSet.change

        :Ожидаемый результат: статус ответа == 200, человек успешно изменён
        """
        human = humans.first()
        url = reverse('human:change', args=[human.id])

        put_data = get_human_data()
        response = apiclient.put(url, put_data)
        assert response.status_code == 200

        human_data = humans.first().jsonify()
        for field, value in put_data.items():
            assert value == human_data[field]

    def test__delete(self, apiclient, humans):
        """
        :Окружение: набор объектов Human
        :Действие: удаление объекта Human с помощью метода HumanViewSet.change

        :Ожидаемый результат: статус ответа == 200, человек успешно удалён
        """
        human = humans.first()
        url = reverse('human:delete', args=[human.id])

        response = apiclient.delete(url)
        assert response.status_code == 200
        assert human not in humans
