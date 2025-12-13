import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)


# Метод isin — проверяет, содержится ли значение в определенном столбце в заданном списке значений.

# Чтобы выбрать строки, где значение в столбце country равно "Italy" или "France", используйте метод:
italy_france_reviews = reviews.loc[reviews.country.isin(["Italy", "France"])]
print(italy_france_reviews)
print()


# Метод notnull — проверяет, является ли значение в столбце не равным NaN (неопределенным или отсутствующим).

# Чтобы выбрать строки, где значение в столбце price не равно NaN,
# т.е. строка содержит значение, используйте метод notnull:
not_null_price_reviews = reviews.loc[reviews.price.notnull()]
print(not_null_price_reviews)
print()


# Можно объединить несколько условий, используя операторы & и | для создания сложных фильтров.

# Рассмотрим пример.Необходимо выбрать строки,
# где значение в столбце country равно "Italy" или "France" и значение в столбце points больше или равно 90:
complex_condition_reviews = reviews.loc[reviews.country.isin(["Italy", "France"]) & (reviews.points >= 90)]
print(complex_condition_reviews)
print()

# Другой пример — требуется выбрать строки, где значение в столбце country равно "Italy"
# или значение в столбце points больше или равно 90, а значение в столбце price не равно NaN:
complex_condition_reviews = reviews.loc[
    ((reviews.country == "Italy") | (reviews.points >= 90)) & (reviews.price.notnull())
]
print(complex_condition_reviews)
print()


# Для присваивания данных в датафрейме используйте обращение через квадратные скобки и имя столбца в виде строки:

# Присвоить значение 'everyone' всем значениям в столбце `critic`
reviews["critic"] = "everyone"

# Создание нового столбца с обратным порядком индексов
reviews["index_backwards"] = range(len(reviews), 0, -1)
