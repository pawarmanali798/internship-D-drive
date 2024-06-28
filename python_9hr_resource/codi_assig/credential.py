

# from typing import  Callable

# def check_validation(input,*pipelines:list[Callable]):
#     for validator in pipelines:
#         if not validator(input):
#             return False
#     return True


# def check_type(data_type):
#     return lambda input:data_type(input)==data_type

# def has_length(length):
#     return lambda input:len(input)==length

# validations_dict={
#     "is_string":check_type(str),
#     "is_integer":check_type(int),
#     "has_length":has_length
# }

# print(check_validation("manali",validations_dict['has_length'](6),validations_dict["is_string"]("manali")))
# print(check_validation("asdfgfhj",validations_dict['has_length'](8)))


def outer_function(data_type):
    def inner_function(input):
        print("input")
    return inner_function #stores reference of inner_function

calling_innerFunction=outer_function(int)
calling_innerFunction("input")

# def check_type(data_type):
#     def inner_function(input):


        