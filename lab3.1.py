while True:
    print("Введите А,B")
    a=float(input())
    b=float(input())
    c=b
    b=a
    a=c
    print(str(a) + " " + str(b))
