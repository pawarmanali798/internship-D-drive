# # import sys
# # def userName(user_name):
# #     name=user_name.len
# #     if(name > 6):
# #         sys.exit("Username is available")#if user name is invalid 
# #     def cred(password):
# #         if(password > 8 and password < 12):
# #             print("Successfully login")
# #         return cred
    
# # credential=userName("manali")
# # print(credential("admin123"))

# def validator(input,*piplines:list[Callable]):
#     for validator in piplines:
#         if(validate==input):
            
        
   
# def check_type(data_type):
#     return lambda input: type(input) == data_type


# def has_length():
#     return lambda input

# validate={
#     is_string: check_type(str)
#     is_integer: check_type(int)
#     has_length: has_length
# }

# print(validator('manali',validate(is_string())))