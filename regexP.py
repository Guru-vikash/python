import re 
str="the rain is spain ieniae@maiai"
x=re.search(r'\w+@\w+',str)
print(x.group())