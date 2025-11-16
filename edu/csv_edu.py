import csv


rows = [["Name", "Age", "Gender"], ["Alice", "25", "Female"], ["Bob", "30", "Male"], ["Charlie", "35", "Male"]]

# Создание и запись файла csv
with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Чтение файла csv
with open("file.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
