import csv

# Необходимо прочитать CSV-файл и вывести на экран информацию о студентах, у которых средний балл больше 4.5.
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row["avg_grade"]) > 4.5:
            print(f"{row['name']} ({row['age']} лет) - средний балл: {row['avg_grade']}")

print()
# Решение наставника
with open("students.csv") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # Пропускаем заголовок таблицы
    for row in reader:
        name, age, avg_grade = row
        if float(avg_grade) > 4.5:
            print(f"{name} ({age} лет) - средний балл: {avg_grade}")
# мое решение получилось проще
