# try:
#     with open("C:\\Users\\bikash\\Desktop\\A.txt","r") as f:
#         with open("C:\\Users\\bikash\\Desktop\\B.txt","w")as f1:    
#             #print(f.readlines())
#             for i in f:
#                 f1.write(i)

# except :
#     print("file not found .plz create file fist ....")
# else:
#     f.close()
#     print("file closed .")
# f=open("C:\\Users\\bikash\\Desktop\\B.txt","r")
# print(f.readline())

import os 
if os.path.exists("C:\\Users\\bikash\\Desktop\\A.txt"):
    os.remove("C:\\Users\\bikash\\Desktop\\A.txt")
    print("file removed")
else:
    print("file not avaiable .")
