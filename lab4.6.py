while True:
    print("Введите A1,B1,C1,A2,B2,C2")
    a1=float(input())
    b1=float(input())
    c1=float(input())
    a2=float(input())
    b2=float(input())
    c2=float(input())
    if (a1==0) and (a2==0) and (b1==b2) and (c1==c2):
        y=c1/b1
        print("y="+str(y))
    else:
        if ((b1!=0) and (b2!=0)) and (a1*b2-a2*b1)!=0:
            y=(a1*c2-a2*c1)/(a1*b2-a2*b1)
            print("y="+str(y))
        else:
            print("y не существует")
    if (b1==0) and (b2==0) and (a1==a2) and (c1==c2):
        x=c1/a1
        print("x="+str(x))
    else:
        if ((a1!=0) and (a2!=0)) and (a1*b2-a2*b1)!=0:
            x=(c1*b2-c2*b1)/(a1*b2-a2*b1)
            print("x=" + str(x))
        else:
            print("x не существует")
