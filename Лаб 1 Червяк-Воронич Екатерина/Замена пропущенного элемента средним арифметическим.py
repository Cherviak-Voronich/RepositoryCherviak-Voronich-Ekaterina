numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_numbers = numbers[:4] + numbers[5:]
sr_znach = round(sum(list_numbers) / len(numbers), 2)
sr_znach = [sr_znach]
new_list = numbers[:4] + sr_znach + numbers[5:]
print("Измененный список:", new_list)
