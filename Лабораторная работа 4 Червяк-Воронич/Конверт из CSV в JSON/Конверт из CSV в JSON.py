# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as f:
        lines = [line for line in csv.DictReader(f)]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as g:
        json.dump(lines, g, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
