while True:
    print("Введите коэффициенты A и B")
    a=float(input())
    b=float(input())
    if a!=0:
        print("x=" + str(-b/a))
    else:
        print("Ошибка: A=0")
