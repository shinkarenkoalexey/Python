x = str(input("n - номер месяца, w - название месяца..."))
if x == "n":
    num = int(input("Номер месяца..."))
    if num in range(1,2) or num == 12: t = "зима"
    if num in range(3,6): t = "весна"
    if num in range(6,9): t = "лето"
    if num in range(9,12): t = "осень"
    if num > 12 or num < 1: print("Такого месяца не существует")
    else: print(num, "месяц -", t)
elif x == "w":
    month = str(input("Название месяца..."))
    num = 0
    if month.lower() == "январь": num = 2
    if month.lower() == "февраль": num = 3
    if month.lower() == "март": num = 4
    if month.lower() == "апрель": num = 5
    if month.lower() == "май": num = 6
    if month.lower() == "июнь": num = 7
    if month.lower() == "июль": num = 8
    if month.lower() == "август": num = 9
    if month.lower() == "сентябрь": num = 10
    if month.lower() == "октябрь": num = 11
    if month.lower() == "ноябрь": num = 12
    if month.lower() == "декабрь": num = 1
    if num in range(1,4): t = "зимы"
    if num in range(4,7): t = "весны"
    if num in range(7,10): t = "лета"
    if num in range(10,13): t = "осени"
    if num == 0: print("Такого месяца не существует")
    else: print(month,"- месяц", t)
else:
    print("Вы ввели что-то не то")

