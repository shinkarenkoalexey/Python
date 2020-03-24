s1 = "***"
# 1 Задание
print("1) 5 + 4 * 5 ** (2 + 2) % 2 = ", 5 + 4 * 5 ** (2 + 2) % 2)
#   1)  5**(2+2) = 5**4 = 625
#   2)  4 * 625 = 2500
#   3)  2500 % 2 = 0
#   4)  5 + 0 = 0

print(s1*5)

# 2 Задание
number1 = 4
number1 = number1 + 4
print("Полное+", number1)

num1 = 4
num1 += 4
print("Краткое+", num1)

print(s1*5)

number2 = 4
number2 = number2 ** 2
print("Полное**", number2)

num2 = 4
num2 **= 2
print("Краткое**", num2)

print(s1*5)

number3 = 5
number3 = number3 * 5
print("Полное*", number3)

num3 = 5
num3 *= 5
print("Краткое*", num3)

print(s1*5)
# 3 Задание
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
print("Привет", name, surname)
