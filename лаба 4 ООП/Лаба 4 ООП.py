CARS_DATABASE = [
    {
        "name": "test_name_1",
        "brand": "test_brand_1",
    },
    {
        "name": "test_name_2",
        "brand": "test_brand_2",
    }
]
if __name__ == "__main__":
    class Car:
        """ Базовый класс машина. """

        def __init__(self, name: str, brand: str):
            self._name = name
            self._brand = brand

        # Публичный метод, который внутри работает с защищенным атрибутом self._name
        @property
        def name(self) -> str:
            return self._name

        # Публичный метод, который внутри работает с защищенным атрибутом self._name
        @name.setter
        def name(self, name: str) -> None:
            if not isinstance(name, str):
                raise TypeError("Название должно быть типа str")
            self._name = name

        # Публичный метод, который внутри работает с защищенным атрибутом self._brand
        @property
        def brand(self) -> str:
            return self._brand

        # Публичный метод, который внутри работает с защищенным атрибутом self._brand
        @brand.setter
        def brand(self, brand: str) -> None:
            if not isinstance(brand, str):
                raise TypeError("Марка машины должен быть типа str")
            self._brand = brand

        def __str__(self):
            return f"Название машины {self.name}. Марка машины {self.brand}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, brand={self.brand!r})"


    class Truck(Car):
        """ Дочерний класс грузовая машина. """
        def __init__(self, name: str, brand: str, lifting_capacity: float):
            super().__init__(name, brand)
            self._lifting_capacity = lifting_capacity

        @property
        def lifting_capacity(self) -> int:
            return self._lifting_capacity

        @lifting_capacity.setter
        def lifting_capacity(self, lifting_capacity: int) -> None:
            if not isinstance(lifting_capacity, (int, float)):
                raise TypeError("Грузоподъемность должна быть типа int или float")
            if lifting_capacity <= 0:
                raise ValueError("Грузоподъемность должна быть больше 0")
            self._lifting_capacity = float(lifting_capacity)

        def __str__(self):
            return f"Название машины {self.name}. Марка машины {self.brand}. Грузоподъемность {self.lifting_capacity}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, brand={self.brand!r}), lifting_capacity={self.lifting_capacity!r})"


    class Passenger(Car):
        """ Дочерний класс легковая машина. """
        def __init__(self, name: str, brand: str, speed: float):
            super().__init__(name, brand)
            self._speed = speed

        @property
        def speed(self) -> int:
            return self._speed

        @speed.setter
        def speed(self, speed: float) -> None:
            if not isinstance(speed, (int, float)):
                raise TypeError("Максимальная скорость должна быть типа int или float")
            if speed <= 0:
                raise ValueError("Максимальная скорость должна быть больше 0")
            self._speed = float(speed)

        def __str__(self):
            return f"Название машины {self.name}. Марка машины {self.brand}. Максимальная скорость {self.speed}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, brand={self.brand!r}), speed={self.speed!r})"
    pass

if __name__ == '__main__':
    # инициализируем список машин
    list_cars = [
        Car(name=car_dict["name"], brand=car_dict["brand"],) for car_dict in CARS_DATABASE
    ]
    for car in list_cars:
        print(car)  # проверяем метод __str__
    print(list_cars)  # проверяем метод __repr__

