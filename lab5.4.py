while True:
    print("Введите числа A,B")
    a=int(input())
    b=int(input())
    if a>b:
        print("Отрезков="+str(int(a//b)))
    else:
        print("Ошибка")
