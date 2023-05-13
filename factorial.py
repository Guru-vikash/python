def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)
    
val=int(input("Enter the value for find factorial :"))
print("Factorial of ",val,"is :",fun(val))