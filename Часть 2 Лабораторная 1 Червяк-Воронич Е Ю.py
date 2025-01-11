# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Pancake:

    """
    Документация на класс.
    Класс представляет Блинчики.
    """

    def __init__(self, pancake_diameter: Union[int, float], quantity: Union[int, float]):

        """
    Инициализирует новый экземпляр.
        Args:
            pancake_diameter [int, float]: диаметр блинчика. Должен быть положительным числом.
            quantity [int, float]: Количество блинчиков. Должен быть положительным числом.
        Example:
        >>> pancake = Pancake(26, 50)

        Raises:
            TypeError: Если диаметр или количество не являются [int, float]
            ValueError: Если диаметр не является положительным числом или количество не является положительным числом.
    """

        self.pancake_diameter = None  # Размер блинчиков
        self.init_pancake_diameter(pancake_diameter)

        if not isinstance(quantity, (int, float)):
            raise TypeError
        if quantity < 0:
            raise ValueError
        self.quantity = quantity  # Количество блинчиков

    def init_pancake_diameter(self, pancake_diameter: Union[int, float]):
        """
        Метод подставляет значение диаметра панкейка
        """
        if not isinstance(pancake_diameter, (int, float)):  # Проверяем, что диаметр типа (int, float)
            raise TypeError     # Вызываем ошибку
        if not pancake_diameter > 0:    # Проверяем, что диаметр больше 0
            raise ValueError    # Вызываем ошибку
        self.init_pancake_diameter = pancake_diameter

    def eaten_pancakes(self, eaten_pancakes: Union[int, float]) -> None:
        """
        Метод вычитает количество блинчиков, которые съели
        """
        if not isinstance(eaten_pancakes, (int, float)):    # Проверяем, что количество съеденных блинчиков типа (int, float)
            raise TypeError     # Вызываем ошибку
        if quantity - eaten_pancakes < 0:
            """
        Проверяем, что количество съеденных блинчиков не превышает изначальное количество
        """
            raise ValueError    # Вызываем ошибку


if __name__ == "__main__":
    pancake = Pancake(20, 100)  # TODO работоспособность экземпляров класса проверить с помощью doctest
    print("Диаметр блинчика: ", pancake.init_pancake_diameter)
    print("Количество блинчиков: ", pancake.quantity)
    pass

print("------------------------------")
class Cake:
    """
        Документация на класс.
        Класс представляет Торты.
    """
    def __init__(self, cost: Union[int, float], weight: Union[int, float]):
        """
            Инициализирует новый экземпляр.
                Args:
                    cost [int, float]: Цена торта. Должна быть положительным числом.
                    weight [int, float]: Вес торта в кг. Должно быть положительным числом.
                Example:
                >>> cake = Cake(4000, 2)

                Raises:
                    TypeError: Если цена или вес не являются [int, float]
                    ValueError: Если цена или вес не является положительным числом.
            """
        self.cost = None  # Цена торта в рублях
        self.init_cost(cost)

        if not isinstance(weight, (int, float)):
            raise TypeError
        if weight < 0:
            raise ValueError
        self.weight = weight  # Вес торта в килограммах

    def init_cost(self, cost: Union[int, float]):
        """
        Метод подставляет значение цены за торт
        """
        if not isinstance(cost, (int, float)):
            raise TypeError
        if not cost > 0:
            raise ValueError
        self.init_cost = cost

    def sale(self, sale: Union[int, float]) -> None:
        """
        Метод расчитывает цену со скидкой
        """
        if not isinstance(sale, (int, float)):
            raise TypeError
        if not sale > 0:
            raise ValueError
        if not sale <100:
            raise ValueError


if __name__ == "__main__":
    cake = Cake(5000, 2.5)  # TODO работоспособность экземпляров класса проверить с помощью doctest
    print("Цена торта в рублях: ", cake.init_cost)
    print("Вес торта в кг: ", cake.weight)
    pass

print("------------------------------")

class Vegetable:
    """
        Документация на класс.
        Класс представляет Овощи.
    """
    def __init__(self, vegetable_name: Union[str], cost: Union[int, float], quantity: Union[int, float]):
        """
            Инициализирует новый экземпляр.
                Args:
                    vegetable_name [str]: Название овоща. Должно быть строкой.
                    cost [int, float]: Цена овощей за 1 кг. Должна быть положительным числом.
                    quantity [int, float]: Количество овощей. Должно быть положительным числом.
                Example:
                >>> vegetable = Vegetable("Помидоры", 160, 4)

                Raises:
                    TypeError: Если цена или количество не являются [int, float], а название овоща не [str]
                    ValueError: Если цена или количество не является положительным числом.
                    """
        if not isinstance(vegetable_name, str):
            raise TypeError
        self.vegetable_name = vegetable_name    # Название овоща
        self.cost = None  # Цена овоща за кг
        self.init_cost(cost)

        if not isinstance(quantity, (int, float)):
            raise TypeError
        if quantity < 0:
            raise ValueError
        self.quantity = quantity  # Количество овощей

    def init_cost(self, cost: Union[int, float]):
        """
        Метод подставляет значение цены овощей за 1 кг
        """
        if not isinstance(cost, (int, float)):
            raise TypeError
        if not cost > 0:
            raise ValueError
        self.init_cost = cost

    def sale(self, sale: Union[int, float]) -> None:
        """
        Метод расчитывает цену со скидкой
        """
        if not isinstance(sale, (int, float)):
            raise TypeError
        if not sale > 0:
            raise ValueError
        if not sale <100:
            raise ValueError


if __name__ == "__main__":
    vegetable = Vegetable("Картошка", 55, 15)  # TODO работоспособность экземпляров класса проверить с помощью doctest
    print("Название овоща: ", vegetable.vegetable_name)
    print("Цена за кг: ", vegetable.init_cost)
    print("Количество овощей: ", vegetable.quantity)
    pass
