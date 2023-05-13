import calc

def decor(func):
	def wrapper(*args):
		print("Name of the function :",func.__name__)
		func(*args)
	return wrapper


#OR
# def decor1(fun):
#     def inner():
#         val=fun()
#         return val+2
#     return inner

# def decor2(fun):
#     def inner():
#         val=fun()
#         return val*2
#     return inner

# @decor2
# @decor1
# def num():
#     return 10

# print(num())
# result=decor1(decor2(num))
# print(result())

