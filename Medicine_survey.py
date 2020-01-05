print("Медицинская анкета")
surname=str(input("Введите фамилию "))
name=str(input("Введите имя "))
age=int(input("Введите ваш возраст "))
weight=float(input("Введите ваш вес "))
while True:
    if age<=30 and 120>=weight>=50:
        print(name, surname, age,"лет", weight,"вес-хорошее состояние")
    elif age<=30 and (weight>120 or weight<50):
        print(name, surname, age,"лет", weight,"вес-срочно на диагностику к врачу")
    elif 40>=age>30 and (weight<=50 or weight>120):
        print(name, surname, age,"лет", weight, "вес-нужно заняться собой")
    elif age>40 and (weight<=50 or weight>120):
        print(name, surname, age,"лет", weight,"вес-требуется врачебный осмотр")
    else:
        print(name,surname, age,"лет", weight,"вес-отличное состояние")
    break
print("Спасибо, что заполнили нашу анкету!")

