number=int(input("Введите число "))
while number>10 or number<0:
    print("Число неверное. Диапазон ввода от 0 до 10.")
    number = int(input("Введите число "))
    if 10>number>0:
        break
number=number**2
print("Квадрат числа равен", number)

