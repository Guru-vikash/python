class MyException(Exception):
    pass

try:
    cash=10000
    withdraw=int(input("Enter withdraw amount :"))
    if withdraw>10000:
        raise MyException("Do not have sufficeint balance .")
    else:
        print(f"You available balance is  {cash-withdraw} rupees  .")
except MyException as s:
    print(s)
else :
    print("divisible by zero")
finally:
    print("finally block")



try:
    f=open('p8.py')
    
    print("file found")
except Exception:
    print("sorry, this file not exist")
else:
    print(f.read())
    f.close()
    print("else block")

class MyExc(Exception):
    def __init__(self):
        print("User doesn't exist !")
    
dic={'bikash':"surat","akash":"odisha","rakesh":"bhubneswar"}
    
try:
    k=input("Enter the name of user :").lower()
    if k in dic:
        print(k,"city is  :",dic[k])
        
    else:
        raise MyExc
except MyExc as e:
    print(e)



class MyExc(Exception):
    def __init__(self):
        print("Not suitable value !")
      
try:
  
    k=int(input("Enter a number :"))
    if k>=0:
        print("Correct !")   
    else:
        raise MyExc

except MyExc as e:
    print(e)