def de_by(val,x):
    l=[]
    while(val!=0):
        rem=val%x
        l.append(rem)
        val=val//x
    l.reverse()
    for i in l:
        print(i,end=" ")
    
    
a=int(input("Enter value to convert :"))
print("Binary is :",end="")
de_by(a,2)
print("\nOcta is :",end="")
de_by(a,8)
print("\nHexaDecimal is :",end="")
de_by(a,16)

# print(bin(a))

# def hexa(val):
#     l=[]
#     while(val!=0):
#         rem=val%8
#         l.append(rem)
#         # val=val//8
#         val=val//16
#     l.reverse()
#     return l
# t=hexa(1000)
# for i in t:
#     print(i,end="")
# print(oct(10))
# print(hex(200))