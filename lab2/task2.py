salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_spend = 0
for _ in range(months):
    total_spend += spend
    spend *= (1 + increase)

total_income = salary * months

money_capital = total_spend - total_income

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.2f}")
