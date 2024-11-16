salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0   # Изначальная подушка безопасности
new_spend = spend   # Новые затраты каждый месяц
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months):
    if i == 0:
        over_zatraty = abs(salary - spend)  # То, насколько новые затраты превышают зп
        money_capital = money_capital + over_zatraty    # Количество денег из финансовой подушки
    else:
        new_spend = new_spend + new_spend * increase
        over_zatraty = abs(salary - new_spend)  # То, насколько новые затраты превышают зп
        money_capital = money_capital + over_zatraty    # Количество денег из финансовой подушки

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
