def add(a,b):
    return "Addition :",(a+b)
def sub(a,b):
    return "Substraction  :",(a-b)
def mul(a,b):
    return "Multiplication :",(a*b)
def div(a,b):
    return "Divison:",(a/b)



a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
x=input("Enter operation(+,-,*,/) :")
if x=="+":
    print(add(a,b))
elif x=="-":
    print(sub(a,b))
elif x=="*":
    print(mul(a,b))
elif x=="/":
    print(div(a,b))
else:
    print("Enter valid input !")

def sum(a,b):
	return (a+b)
def sub(a,b):
	return(a-b)
def mul(a,b):
	return (a*b)
def div(a,b):
	return (a/b)
def squ(a):
	return (a*a)
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print()
if a<b or b<a or a==b:
	print("addition =",sum(a,b))
	if a<b:
		print("we can substract ")
	else:
		print("substraction =",sub(a,b))

	print("multiplication =",mul(a,b))
	print("Division =",div(a,b))
	print("squar root  =",squ(a))







def prime(n):
	l=[]
	c=0
	for i in range(1,n+1):
		if n%i==1:
			c+=1
	if(c==2):
		l.append(i)
	else:
		print("not prime")
	retrun l	
k=[12,5,7,23,24]
for i in range(0,len(k)):
	prime(k[i])

