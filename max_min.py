def find(a,b,c):
    if a>b and a>c:
        print(a,"a is greater .")
        if b>c:
            print(c," is smaller .")
        else:
            print(a," is smaller .")
    elif b>c and b>a:
        print(b," is greater .")
        if a>c:
            print(c," is smaller .")
        else:
            print(a," is smaller .")
    elif c>a and c>b:
        print(c," is greater .")
        if b>a:
            print(a," is smaller .")
        else:
            print(b," is smaller .")
    else :
        print("all are same .")

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
find(a,b,c)