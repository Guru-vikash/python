# def vowel(lst):
#     l=["a","e","i","o","u"]
#     count=0
#     for i in lst:
#         if i.lower() in l:
#             count+=1
#     return count
# print("Number of vowels in the string :",vowel("Kaushitamam"))

# def length(s):
#     count=0
#     for i in s:
#         count+=1
#     return count
# print("Lenght of word is =",length("Jayanamam"))

# print("PrasantSir"[::-1])

# l="Bikash pradhan"
# x=l.replace("Bikash","Akash")
# print(x)

s=str(input("Enter a string :"))
rev=s[::-1]
if s==rev:
    print(" String is palindrome ")
else:
    print("String is not a palindrome ")