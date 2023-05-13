
def prime(lst):
    l=[]
    for i in lst:
        if i==0 and i==1:
            continue
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            l.append(i)
    return l
lst=[1,3,5,37,55,6,90,40]
x=map(prime,lst)
print(prime(lst))



