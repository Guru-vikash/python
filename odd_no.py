# def find_odd():
list=[]
l=[]
c=0
print("Enter your 10 values :")
for i in range(0,11):
    x=int(input())
    list.append(x)
print("List is = ",list)
for i in list:
    if i%2==1:
        l.append(i)
        
if(len(l)!=0):  #chech the length of list is not zero
    print("List of the Odd numbers = ",l)
else:
    print("No odd no. is found.")