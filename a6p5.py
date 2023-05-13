l=[1,2,3,5]
l1=[10,23,34,44]
l2=[] #3rd list
for i in range(len(l)):
    sum=l[i]+l1[i]  #sum of list elements
    l2.append(sum)
print("sum of two list elements :",l2)
