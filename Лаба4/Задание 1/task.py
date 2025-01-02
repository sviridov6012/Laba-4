class Vehicle:
    """ Базовый класс для транспортных средств. """

    def __init__(self, brand: str, model: str, year: int):
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    def vehicle_info(self) -> str:
        """ Возвращает общую информацию о транспортном средстве. """
        return f"{self.year} {self.brand} {self.model}"

    def __str__(self):
        return f"Транспортное средство: {self.vehicle_info()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"


class Car(Vehicle):
    """ Класс для легковых автомобилей. """

    def __init__(self, brand: str, model: str, year: int, doors: int):
        super().__init__(brand, model, year)
        self.doors = doors

    @property
    def doors(self) -> int:
        return self._doors

    @doors.setter
    def doors(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество дверей должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество дверей должно быть положительным.")
        self._doors = value

    def vehicle_info(self) -> str:
        """ Возвращает информацию о легковом автомобиле, включая количество дверей. """
        return f"{super().vehicle_info()} | Дверей: {self.doors}"

    def __str__(self):
        return f"Легковой автомобиль: {self.vehicle_info()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, doors={self.doors!r})"


class Truck(Vehicle):
    """ Класс для грузовых автомобилей. """

    def __init__(self, brand: str, model: str, year: int, capacity: float):
        super().__init__(brand, model, year)
        self.capacity = capacity

    @property
    def capacity(self) -> float:
        return self._capacity

    @capacity.setter
    def capacity(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Грузоподъемность должна быть числом с плавающей запятой.")
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть положительной.")
        self._capacity = float(value)

    def vehicle_info(self) -> str:
        """ Возвращает информацию о грузовом автомобиле, включая грузоподъемность. """
        return f"{super().vehicle_info()} | Грузоподъемность: {self.capacity} тонн"

    def __str__(self):
        return f"Грузовой автомобиль: {self.vehicle_info()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, capacity={self.capacity!r})"


# Пример использования классов
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 4)
    truck = Truck("Volvo", "FH", 2019, 18.0)

    print(car)  # Легковой автомобиль: 2020 Toyota Camry | Дверей: 4
    print(truck)  # Грузовой автомобиль: 2019 Volvo FH | Грузоподъемность: 18.0 тонн
