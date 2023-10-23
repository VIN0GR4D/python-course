money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

current_budget = money_capital + salary
months = 0

while current_budget - spend >= 0:
    current_budget -= spend
    spend += spend * increase
    current_budget += salary
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
