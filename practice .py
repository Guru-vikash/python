# result=[i**2 for i in range(11) if i%2==0]
# print(result)

#or
# string='HimanshuKumarJena'
# dic={}
# for i in string:
#     key=i
#     val=string.count(i)
#     dic.update({key:val})

# print(dic)

#or
# l=[11,12,13,14,15,16,17,18,19,20,21,22]
# result=list(filter(lambda x:x%2==0,l))
# print(result)

#or
student=[(12,50,'himansu'),(13,70,'rakesh')]
print(student[1])
n=eval('input("Enter student details :")')
student.append(n)
print(student)
print(student[2])