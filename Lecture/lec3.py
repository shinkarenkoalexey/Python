"""
    1. Напишите и вызовите функцию, передав в нее два аргумента "Изучаем" и "Python",
      положите результат в переменную и выведите ее значение на экран.
    Сделайте так, чтобы результирующая строка выводилась заглавными буквами.
"""
def learnpython(word, language):
    result = ("{} {}".format(word.upper(), language.upper()))
    print(result)


learnpython("Изучаем", "Python")

""" 
    2. Создайте функцию format_price, которая принимает один аргумент price.
    Приведите price к целому числу. Верните строку "Цена: ..... руб."
    Вместо многоточия вставьте полученное целое число.
    Вызовите функцию, передав на вход 56.24 и положите результат в переменную.
    Выведите значение переменной с результатом.
"""
def format_price(price):
    result = ("Цена: {} руб.".format(int(price)))
    print(result)


format_price(56.24)
