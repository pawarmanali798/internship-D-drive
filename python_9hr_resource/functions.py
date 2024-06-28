# def greet(first,last):
#     print(f"{first} {last}")
    
    
# greet("manali","pawar")

# #factorial
# n=input("Enter the input:")
# input=int(n)
# fact=1
# for num in range(1,input+1):
#     fact=fact*num
# print(fact)


#even&odd
def check_evenOdd(input):
    if input%2==0:
        print("number is even")
    else:
        print("number is odd")


num=input("Enter the number:")
input=int(num)
check_evenOdd(input)