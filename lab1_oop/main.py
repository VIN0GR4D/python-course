import doctest

class Watch:
    def __init__(self, brand: str, waterproof: bool):
        """
        Инициализация часов.

        :param brand: Марка часов.
        :param waterproof: Водонепроницаемость.

        Примеры:
        >>> watch = Watch("Casio", True)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка часов должна быть строкой")
        if not isinstance(waterproof, bool):
            raise TypeError("Водонепроницаемость должна быть булевым значением")
        self.brand = brand
        self.waterproof = waterproof

    def setTime(self, hours: int, minutes: int):
        """
        Устанавливает время на часах.

        :param hours: Часы.
        :param minutes: Минуты.

        Примеры:
        >>> watch = Watch("Casio", True)
        >>> watch.setTime(10, 30)
        """
        if not isinstance(hours, int) or not (0 <= hours < 24):
            raise ValueError("Часы должны быть целым числом от 0 до 23")
        if not isinstance(minutes, int) or not (0 <= minutes < 60):
            raise ValueError("Минуты должны быть целым числом от 0 до 59")
        ...

    def showTime(self) -> str:
        """
        Показывает текущее время.

        :return: Текущее время в формате 'HH:MM'.

        Примеры:
        >>> watch = Watch("Casio", True)
        >>> watch.showTime()
        '10:30'
        """
        ...

class Wardrobe:
    def __init__(self, material: str, shelves: int):
        """
        Инициализация шкафа.

        :param material: Материал изготовления.
        :param shelves: Количество полок.

        Примеры:
        >>> wardrobe = Wardrobe("Дерево", 5)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(shelves, int) or shelves < 0:
            raise ValueError("Количество полок должно быть неотрицательным целым числом")
        self.material = material
        self.shelves = shelves

    def addClothes(self, clothes: str):
        """
        Добавляет одежду в шкаф.

        :param clothes: Название одежды.

        Примеры:
        >>> wardrobe = Wardrobe("Дерево", 5)
        >>> wardrobe.addClothes("Пальто")
        """
        ...

    def removeClothes(self, clothes: str):
        """
        Удаляет одежду из шкафа.

        :param clothes: Название одежды.

        Примеры:
        >>> wardrobe = Wardrobe("Дерево", 5)
        >>> wardrobe.removeClothes("Пальто")
        """
        ...

class Bed:
    def __init__(self, size: str, material: str):
        """
        Инициализация кровати.

        :param size: Размер кровати.
        :param material: Материал изготовления.

        Примеры:
        >>> bed = Bed("Двуспальная", "Дерево")
        """
        if not isinstance(size, str):
            raise TypeError("Размер должен быть строкой")
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.size = size
        self.material = material

    def makeBed(self):
        """
        Застелить кровать.

        Примеры:
        >>> bed = Bed("Двуспальная", "Дерево")
        >>> bed.makeBed()
        """
        ...

    def changeSheets(self, sheets: str):
        """
        Поменять постельное белье.

        :param sheets: Тип постельного белья.

        Примеры:
        >>> bed = Bed("Двуспальная", "Дерево")
        >>> bed.changeSheets("Хлопок")
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
