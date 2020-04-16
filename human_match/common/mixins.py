class JsonMixin:
    def jsonify(self) -> 'dict':
        """Возвращает данные о записи в виде словаря."""
        return self.__class__.objects.filter(id=self.id).values().first()