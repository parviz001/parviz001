while True:
    print("Введите вес конфет X стоимостью A рублей")
    x=float(input())
    a=float(input())
    print("Введите Y кг конфет")
    y=float(input())
    if x!=0:
        print("1кг стоит " + str(a/x) + " Р")
        print(str(y) + "кг стоит " + str(a*y/x) + " Р")
    else:
       print("Ошибка")
