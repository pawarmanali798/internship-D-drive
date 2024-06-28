from utils import find_max

user_input=input("Enter the numbers separating by comma:")

userInput=user_input.split(",")

list_Numbers=[]
for number in userInput:
    list_Numbers.append(int(number))

print(find_max(list_Numbers))
