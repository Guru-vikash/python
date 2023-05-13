x=int(input("Enter you number :"))
lst=str(x)

sum=0
for i in lst:
    sum+=int(i)**len(lst)

if sum==x:
    print( x," is an armstrong number .")
else:
    print( x," is not armstrong number .")