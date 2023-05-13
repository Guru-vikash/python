def c_f(cel):
    fer=(1.8*cel)+32
    return fer
def f_c(fer):
    cel=(fer-32)/1.8
    return cel

ch=input("Enter c or f to convert temperature (c=celsius and f=faherheit):")
val=int(input("Enter the value :"))
if ch=='f':
    print(val," degree faherheit  :",f_c(val)," celsius ")
elif ch=='c':
    print(val,"degree celsius  :",c_f(val)," faherheit")
else:
    print("Invalid input! ")