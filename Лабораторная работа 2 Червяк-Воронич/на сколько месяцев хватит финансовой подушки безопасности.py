money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0 #количество месяцев, на которое хватит подушки безопасности
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
budjet = money_capital + salary # Бюджет первого месяца
while budjet >= spend:
    if count == 0:
        budjet = budjet + salary - spend  # Подушка безопасности после первого месяца
        count += 1
    else:
        spend = spend + spend * increase    # Новые траты за месяц
        budjet = budjet + salary - spend    # Бюджет после трат в месяце
        count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
