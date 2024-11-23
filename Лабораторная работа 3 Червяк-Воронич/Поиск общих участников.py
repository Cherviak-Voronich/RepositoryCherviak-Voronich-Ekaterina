# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, rasd=","):
    intersection_set = list(set(first.split(rasd)).intersection(set(second.split(rasd))))
    intersection_set.sort()
    return intersection_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, rasd="|"))
