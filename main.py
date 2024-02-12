class Car:
    """Базовый класс автомобиля.

    Атрибуты:
    - brand (str): Марка автомобиля.
    - model (str): Модель автомобиля.
    - release_year (int): Год выпуска автомобиля.
    """

    def __init__(self, brand: str, model: str, release_year: int):
        self._brand = brand  # Инкапсулировано для контроля доступа к марке автомобиля
        self._model = model  # Инкапсулировано для контроля доступа к модели автомобиля
        self._release_year = release_year  # Инкапсулировано для контроля доступа к году выпуска автомобиля

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def release_year(self) -> int:
        return self._release_year

    def __str__(self) -> str:
        return f"Марка автомобиля {self.brand}, модель {self.model}, год выпуска {self.release_year}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}," \
               f"release_year={self.release_year!r})"

    def calculate_insurance(self, base_rate: int) -> int:
        """Вычисляет стоимость страховки на основе базовой ставки и возраста автомобиля."""
        age = 2024 - self._release_year
        return base_rate + age * 100


class LightCar(Car):
    """Класс для легковых автомобилей, наследуется от Car.

    Атрибуты:
    - body_type (str): Тип кузова автомобиля.
    - passenger_capacity (int): Вместимость пассажиров.
    """

    def __init__(self, brand: str, model: str, release_year: int, body_type: str, passenger_capacity: int):
        super().__init__(brand, model, release_year)
        self._body_type = body_type  # Инкапсулировано для определения типа кузова с возможностью контроля изменений
        self._passenger_capacity = passenger_capacity  # Инкапсулировано для определения вместимости пассажиров
        # с контролем изменений

    @property
    def body_type(self) -> str:
        return self._body_type

    @property
    def passenger_capacity(self) -> int:
        return self._passenger_capacity

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, тип кузова {self.body_type}, вместимость пассажиров {self.passenger_capacity}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}," \
               f"release_year={self.release_year!r}, body_type={self.body_type!r}," \
               f"passenger_capacity={self.passenger_capacity!r})"

    def calculate_insurance(self, base_rate: int) -> int:
        """Перегружает стоимость страховки, учитывая тип кузова и вместимость пассажиров.

        Обоснование перегрузки: Для легковых автомобилей тип кузова и вместимость пассажиров могут значительно влиять
        на риски, связанные со страхованием, и, соответственно, на стоимость страховки.
        """
        base_insurance = super().calculate_insurance(base_rate)
        if self._body_type == "седан":
            return base_insurance + 200
        elif self._passenger_capacity > 5:
            return base_insurance + 500
        return base_insurance


if __name__ == "__main__":
    # Write your solution here
    pass
