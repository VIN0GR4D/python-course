from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass1 = Glass(200, 100)
    print(f"Glass1: {glass1.capacity_volume} ml, {glass1.occupied_volume} ml")

    glass2 = Glass(200, 150)
    print(f"Glass2: {glass2.capacity_volume} ml, {glass2.occupied_volume} ml")

    print("Доливаем воды в первый стакан...")
    glass1.occupied_volume += 50
    print(f"Glass1 после добавления воды: {glass1.capacity_volume} ml, {glass1.occupied_volume} ml")
    print(f"Glass2 остается неизменным: {glass2.capacity_volume} ml, {glass2.occupied_volume} ml")

    same_object = glass1 is glass2
    print(f"glass1 и glass2 это один и тот же объект? {same_object}")
