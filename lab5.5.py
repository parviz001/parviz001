while True:
    print("Введите числа A,B")
    a=int(input())
    b=int(input())
    if a>b:
        print("Незанятая часть=" + (str(a-a//b*b)))
    else:
        print("Ошибка")
