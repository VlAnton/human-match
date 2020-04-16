# Human-Match app

## Запуск проекта
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## Приложения

### Human app
`human/` — список существующих Human
`human/create` — создание Human
`human/<int:pk>` — получение данных по Human
`human/<int:pk>/change` — изменение Human
`human/<int:pk>/delete` — удаление Human


### Match app
`match/` — получение списка Match c вложенным Human
`match/<int:human_id>` — получение Match для данного human_id
