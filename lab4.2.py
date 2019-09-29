while True:
    print("Введите угол")
    a=float(input())
    if a>0 and a<360:
        print("Угол в радианах =" + str(a/180) + "π")
    else:
        print("Ошибка")
