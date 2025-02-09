class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = None   # делаем атрибут защищенным, добавив нижнее подчеркивание
        self.set_name(name)    # устанавливаем с помощью метода название книги
        self._author = None  # делаем атрибут защищенным, добавив нижнее подчеркивание
        self.set_author(author)  # устанавливаем с помощью метода автора

    # Публичный метод, который внутри работает с защищенным атрибутом self._name
    def get_name(self) -> int:
        return self._name

    # Публичный метод, который внутри работает с защищенным атрибутом self._name
    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self._name = name

    # Публичный метод, который внутри работает с защищенным атрибутом self._author
    def get_author(self) -> int:
        return self._author

    # Публичный метод, который внутри работает с защищенным атрибутом self._author
    def set_author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError("Автор должен быть типа str")
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> int:
        return self.duration

    @duration.setter
    def duration(self, duration: int) -> None:
        if not isinstance(duration, int):
            raise TypeError("Продолжительность книги должна быть типа int")
        if duration <= 0:
            raise ValueError("Продолжительность книги должна быть больше 0")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), duration={self.duration!r})"
