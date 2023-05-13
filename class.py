# class Employee:
#     def __init__(self,fist,last):             //this mehtod __init__ is default constructor of class
#         self.fist=fist
#         self.last=last
#         self.email=fist+"-"+last+"@gmail.com"

#     def fullname(self):
#         return "{} {} {}".format(self.fist,self.last,self.email)
    
# emp_1=Employee("bikas","pardhan")
# print(emp_1.fullname())

# class A(object):
#    #"Learn coding"
#     age=21
#     def fun(self):
#         name='Learn coding'
#         print(name)

# obj=A()
# print(obj.fun())
#print(obj.__doc__)

class Employee:
    num_of_emp=0
    raise_amt=1.04
    def __init__(self,fist,last ,pay):
        self.fist=fist
        self.last=last
        self.emal=fist +"-"+last+"@gmial.com"
        self.pay=pay
        Employee.num_of_emp+=1

    def fullname(self):
        return "{} {}".format(self.fist,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay *self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

emp1=Employee("bikash","pradhan",2000)
emp1=Employee("Akash","pradhan",4000)
print(emp1.fullname())
print(emp1.raise_amt)
emp1.set_raise_amt(1.05)

emp_str_1='john-Doe-7000'
emp_str_2='bikash-rpa-38899'

first,last,pay=emp_str_1.split('-')
new=Employee(first,last,pay)

print(emp_str_1.emal)
print(emp_str_1.pay)
