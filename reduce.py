import functools
import operator
l=[21,22,23,24,25,26,27,28,29,30,31,32]
print("sum :")
print(functools.reduce(lambda a,b:a+b,l))
print("max")
print(functools.reduce(lambda a,b:a if a>b else b,l))
print('sum of the list using operatior addition :')
print(function.reduct(operator.add,l))

from functools import reduce
def re(x,y):
    return x+y

ans=reduce(re,[2,3,4,5,6])
print(ans)