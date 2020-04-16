import pytest

from django.urls import reverse


pytestmark = pytest.mark.django_db


class TestMatchViewSet:
    """Набор тестов для MatchViewSet."""

    def test__retreive__correct_data(self, apiclient, humans):
        """
        :Окружение: Набор существующих людей
        :Данные: ids существующих людей
        :Действие: получение пары human, match с помощью метода MatchViewSet.retreive

        :Ожидаемый результат: статус ответа == 200
        """
        human_ids = humans.values_list('id', flat=True)
        for human_id in human_ids:
            url = reverse('match:detail', args=[human_id])
            response = apiclient.get(url)
            assert response.status_code == 200

    def test__retreive__incorrect_data(self, apiclient):
        """
        :Окружение: Набор существующих людей
        :Данные: ids существующих людей
        :Данные: id несуществующего человека
        :Действие: получение пары human, match с помощью метода MatchViewSet.retreive

        :Ожидаемый результат: статус ответа == 404
        """
        incorrect_id = 1
        url = reverse('match:detail', args=[incorrect_id])
        response = apiclient.get(url)
        assert response.status_code == 404


    def test__list(self, apiclient, humans):
        """
        :Окружение: Набор существующих людей
        :Данные: ids существующих людей
        :Действие: получение пары human, match с помощью метода MatchViewSet.retreive

        :Ожидаемый результат: статус ответа == 200
        """
        url = reverse('match:list')
        response = apiclient.get(url)
        assert response.status_code == 200
