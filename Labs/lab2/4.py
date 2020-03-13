num = int(input("Введите код символа..."))
if num in range(65,91) or num in range(97,123):
    print("Код английской буквы - ", chr(num))
else:
    print("Ваш символ -", chr(num))
