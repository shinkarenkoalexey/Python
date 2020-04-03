n = int(input("Сумма займа = "))
p = float(input("Процент = ")) / 100
y = int(input("На сколько лет? ")) * 12


m = (n + n * p) / y
s = m * y
print("Месячный платеж =", m)
print("Суммарная выплата =", s)