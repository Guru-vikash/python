import calc
import decor 

# result1 = decor.decor(calc.add)
# print(result1())
# print(calc.add())
# result2=decor.decor(calc.sub)
# print(result2())
# print(calc.sub())
# result3 = decor.decor(calc.mul)
# print(result3())
# print(calc.mul())
# result4 = decor.decor(calc.div)
# result4()
# print(calc.div())

try:
    result1=decor.decor(calc.add)
    result1()
    # print(calc.dod())
  
except AttributeError as e:
    print("File not exist")