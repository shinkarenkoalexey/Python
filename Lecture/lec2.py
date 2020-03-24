# 1 Задание
name = "\"Д'Артаньян и три мушкетера\""
print("Книгу", name, "написал А.Дюма")

# 2 Задание
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
print("Привет, {} {}!".format(name, surname))
print("Ваши инициалы: {}{}.".format(name[0].upper(), surname[0].upper()))
print("Один вывод:")
print("Привет, {} {}!".format(name, surname)+"\nВаши инициалы: {}{}.".format(name[0].upper(), surname[0].upper()))