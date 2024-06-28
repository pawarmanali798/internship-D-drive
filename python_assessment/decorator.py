# #transaction
from datetime import datetime
def decorator(hello):
    def wrapper():
        print("Transaction initiated")
        hello()
        print("Transaction completed")
    return wrapper

@decorator#hello=decorator(hello)
def hello():
    print("Executing steps")
    
hello()



# #logtime
# def log_time(func):
#     def inner_func(*args):
#         print(datetime.now())
#         func(*args)
#     return inner_func
    

# @log_time
# def save_user(user):
#     print(f"saved the users {user}")

# @log_time
# def save_products(product):
#     print("saved products")
    
# save_user("ADMIN")

# save_products(2)


# #authorization
# def authorization(list_ofRoles):
#     def authority(func):
#         def able_toDelete(*args):
#             if args[0] in list_ofRoles:
#                 return func(*args)
#             return "INVALID"
#         return able_toDelete
#     return authority
            

# @authorization(["admin","hr","intern"])
# def authority(user):#the enter inside this will be only when if is satisfied and imp returns func()
#     print("You are authorized to delete")
#     return f"Authorized {user}"
    
# print(authority("hr"))


def decorator(func):
    def wrapper():
        print("Transcation initiated")
        func()
        print("Transcation completed")
    return wrapper

@decorator
def hello():
    print("Executing transcation")

hello()


















    