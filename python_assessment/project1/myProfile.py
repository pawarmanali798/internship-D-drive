# user="admin"

# from typing import Callable


# def authority(input,*members: list[Callable]):
#     for member in members:
#         if not member(input):
#             return False
#     return True

# def check_user(str):
#     return "Profile deleted successfully"

# def check_userIntern(str):
#     return "Not able to delete the profile"


# my_profile={
#     "user_admin":check_user("str"),
#     "user_intern":check_userIntern("str")
# }

# print(authority("user",my_profile["user_admin"],my_profile["user_intern"]))


# def check_user(input):
#     if input=="admin" or input=="hr" or input=="hr":
#         print("Profile deleted successfully")
#     else:
#         print("Do not have access to delete")
    

# my_profile={
#     "user_admin":check_user(""),
#     "user_hr:check":check_user(""),
#     "user_intern":check_user(""),
#     "user_developer":check_user(""),
#     "user_stakeHolder":check_user("")
# }
# print(my_profile["user_hr"])

def outer_func(func):
    print("executed outer_func")
    def middle():
        print("executed middle_func")
    return middle

@outer_func
def message():
    print("executed middle_func")


    