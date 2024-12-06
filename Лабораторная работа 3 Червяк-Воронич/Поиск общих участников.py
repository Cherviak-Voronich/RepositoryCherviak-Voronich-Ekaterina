# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, rasd=","):
    first_group = set(first.split(rasd))    # Разделение первой группы
    second_group = set(second.split(rasd))  # Разделение второй группы
    intersection_set = list(first_group.intersection(second_group))     # Поиск пересечений между группами
    intersection_set.sort()
    return intersection_set

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, rasd="|"))
