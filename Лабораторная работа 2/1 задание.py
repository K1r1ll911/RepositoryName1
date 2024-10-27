salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
a = 0
for month in range(months):
    deficit = spend - salary
    if deficit > 0:
       a += deficit
    spend *= (1 + increase)
a = round(a)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", a)
