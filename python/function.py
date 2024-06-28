def add(n1,n2):
    return n1 + n2
add()


add #=>reference to body of function.....everything after function name
add(5,3)#executes code at reference

add_fn=add
print(add_fn(5,3))

#lambda
#


#return type and parameters of callable

# from typing import Callable

divide=Callable[[int,int],int]=lambda n1,n2:n1/n2 #parameters for callable
"""param: n1 int, param: n2 int"""
divide__doc__="""param:n1 int, param: n2 int"""

divide(10,5)

from typing import TypeVar

T=TypeVar('T')
    

def find(array:list[T],elem:T)-> T|None:
    for elem_in_array in array:
        if elem ==elem_in_array:
            return elem
        
find([1,2,3,4,5],3)


#loanfactory to calculate emi
def loanFactory(rate_of_interest):
    def calculate(principle_amt,years):
        return principle_amt*rate_of_interest*years
    return calculate

car_loan=loanFactory(8)
print(car_loan(2000,3))



#now without changing anything in existed function change the rate of interest outside the function and should calculate with updated rate
def loanFactory(rate_of_interest):

    def calculate(principle_amt,years):
        return principle_amt*rate_of_interest*years
    

    def updated_rate(rate):
        nonlocal rate_of_interest
        rate_of_interest=rate
    return [calculate, updated_rate] # this reference will help in line 65

car_loan,updated_rate=loanFactory(8)
updated_rate(2) # this will help to calculate def updated_rate
print(car_loan(2000,3))

# arr =loanFactory(8)
# car_loan = arr[0]
# updated_rate = arr[1]



# print(car_loan(2000,3))

# home_loan_emi=loanFactory(10)
# personal_loan_emi=loanFactory(12)

# print(car_loan_emi(20000,3))
# print(home_loan_emi(20000,3))
# print(personal_loan_emi(20000,3))


# def sub(n1:int,n2:int) -> int:
#     return n1 - n2
# sub(10,2)

# def multiply(n1:int,n2:int) -> int:
#     """this fn  multiplies two no."""
#     return n1 * n2
# multiply()



