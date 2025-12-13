import pandas as pd

# Часто данные уже существуют и хранятся в различных форматах, таких как CSV и Excel.
# Мы можем использовать функцию pd.read_csv() для чтения данных из файла CSV
# и pd.read_excel() для чтения данных из Excel.

# Пример чтения CSV-файла
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

# Чтобы получить информацию о размерности DataFrame или Series,
# то есть о количестве строк и столбцов, используется атрибут shape
print(wine_reviews.shape)  # shape возвращает кортеж, где первое значение - кол-во строк, второе - кол-во столбцов

print()
# Метод head() — по умолчанию выводит первые пять строк таблицы.
print(wine_reviews.head(3))  # Вы можете указать другое количество строк в аргументе.

print()
# Пример чтения Excel-файла
excel_data = pd.read_excel("winemag-data-130k-v2.xlsx")
print(excel_data.shape)
print(excel_data.head())

# Мы можем выбрать конкретный лист из Excel-файла при его чтении.
# Для этого нужно указать название листа в параметре sheet_name
excel_data_specific_sheet = pd.read_excel("winemag-data-130k-v2.xlsx", sheet_name="Лист 1 - winemag-data-130k-v2")
print(excel_data_specific_sheet.head())

# Также можно указать столбец, который следует использовать в качестве индекса.
# Для этого необходимо указать в параметре index_col номер колонки, которая будет использоваться в качестве индекса
excel_data_with_index = pd.read_excel("winemag-data-130k-v2.xlsx", index_col=0)
print(excel_data_with_index.head())
