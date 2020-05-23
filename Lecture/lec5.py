print("Задание 1\n")

group1 = ["Шинкаренко Алексей", "Грачева Диана", "Фукалова Анастасия", "Юркевич Даниил", "Петренко Оскар", "Калапкина Татьяна", "Рымшина Екатерина", "Сынкова Кристина", "Миндиярова Аделя", "Акимцев Даниил"]
group2 = ["Евтеева Анастасия", "Горшкова Анна", "Нужин Даниил", "Чинакаев Ринат", "Чернов Константин", "Гужова Ксения", "Иванова Ангелина", "Попова Анастасия", "Торосова Диана", "Власова Полина"]
sport = tuple(group1[::2]) + tuple(group2[::2])      # Создание кортежа
print(group1)
print(group2)
print(sport)
print("Длина кортежа -", len(sport))
sport_sort = tuple(sorted(sport))     # Сортировка кортежа и преобразование списка в кортеж
print(sport_sort)
sport_str = ' '.join(sport_sort).split(" ")    # Разделение имени и фамилии
if sport_str.count("Анастасия") == 0:     # Подсчет количества имен Анастасия в команде
    print("Людей с таким именем в команде нет")
else:
    print("Людей с именем Анастасия - ", sport_str.count("Анастасия"))
if sport_str.count("Иванов") == 0:     # Подсчет количества фамилий Иванов в команде
    print("Людей с такой фамилией в команде нет")
else:
    print("Людей с фаимлией Иванов - ", sport_str.count("Иванов"))

print("\nЗадание 2\n")

capital = {
    "Китай": "Пекин",
    "Азербайджан": "Баку",
    "Австрия": "Вена",
    "Великобритания": "Лондон",
    "США": "Вашингтон",
    "Турция": "Анкара",
    "Япония": "Токио",
    "Германия": "Берлин",
    "Дания": "Копенгаген",
    "Египет": "Каир",
    "Израиль": "Иерусалим",             # Создание словаря
    "Италия": "Рим",
    "Казахстан": "Астана",
    "Канада": "Оттава",
    "Беларусь": "Минск",
    "Бразилия": "Бразилиа",
    "Венгрия": "Будапешт",
    "Латвия": "Рига",
    "Мексика": "Михико",
    "Польша": "Варшава",
    "Россия": "Москва"
}

print(capital)     # Вывод словаря
print("Столица Египта - ", capital.get("Египет"))     # Вывод столицы Египта

country_sort = sorted((value, key) for (value, key) in capital.items())    # Сортировка по стране

capital_sort = sorted(capital.items(), key=lambda i: i[1])    # Сортировка по столице

print("\nСортировка по столице:")

for j in capital_sort:
    print(j[0], ":", j[1])

print("\nСортировка по стране:")

for k in country_sort:
    print(k[0], ":", k[1])


