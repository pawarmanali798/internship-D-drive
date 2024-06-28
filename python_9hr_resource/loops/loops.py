#break
# value=1
# while value < 10:
#     if value == 5:
#         break
#     print(value)
#     value+=1


# continue
# value=1
# while value <= 10:
#     value += 1
#     print(value)
#     if value == 5:
#         continue
# else:
#         print("now its " + str(value))

#for loop
# names=["leo","don","snow"]
# for pets in names:
#     if pets == "don":
#         break
# print(pets)

#for loop range
# for x in range(4):
#     print(x)
    
    
# for x in range(2,7): #last value is excluded
#     print(x)



# for x in range(0,100,5):
#     print(x)

# names=["leo","don","snow"]
# actions=["plays","eats","walks"]


# for action in actions:
#     for name in names:
#         print(name + " " + action)

# for x in range(10):
#     print(x)
# print(type(range))# class type

# add=0
# for item in [10,20,30]:
#     add=add+item
# print(add)

# stars=[5,2,5,2,2]

# for count in stars:
#     output=''
#     for x in range(count):
#         output+='*'
#     print(output)# print(*) in F shape
        

# list=[10,20,30]
# output=''
# for x in list:
#     output+=str(x)
    
# print(output)#102030

# list=[1,1,1,5]
# for count in list:
#     output=''
#     for x in range(count):
#         if count==5:
#             output+='*'
#         print(output)
#     else:
#             print('*')

# list=[1,1,1,5]
# for count in list:
#     output=''  
#     for x in range(count):  # Use the inner loop to repeat '*' count times
#         output += '*'
#     print(output)# L shape * print

# list=[100,3,100,20,4000,700]

# largest=list[0]
# for x in list:
#     if x > largest:
#         largest=x
# print(largest)#4000

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
# print(matrix[0][2])
# matrix[0][2]=40
# print(matrix[0][2])
# print(matrix)

# print('---'*4)

# list=[10,20,30,40]
# print(list)
# list[3]=0
# print(list)


# matrix=[
#     [1,2,3],
#     [4,50,6],
#     [7,8,9]
# ]
# largest=matrix[0][0]
# for row in matrix:
#     for item in row:
#         if item > largest:
#             largest=item
# print(largest)

# list=[2,4,6,8,4]

# for x in list:
#     if x == range

#tuples

#remove duplicates
# list=[2,4,6,8,2,6,10,6]
# unique=[]
# for item in list: 
#     if item not in unique:
#         unique.append(item)
# print(unique)

# tup=(10,20,30)
# x=tup.count(20)
# print(x)

customer={
    "name":"Manali",
    "age":22,
    "is_verified":True
}

customer["name"]="himali"
print(customer.get("birthdate","April 30"))
print(customer)

# #input 1234=>one two three

# def phone_to_number(phone):
#     dict_phone={
#     "1":"one",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five",
#     "6":"Six",
#     "7":"Seven",
#     "8":"Eight",
#     "9":"Nine",
# }
#     output=" "
#     for number in phone:
#         output+=dict_phone.get(number,"!")
#     return output.strip()

# phoneNumber=input("Enter the phoneno:")
# print(phone_to_number(phoneNumber))


# def emoji_converter(user_in):
#     words=user_in.split(' ')
#     emojis={
#     ":)":"😁",
#     ":(":"😌",
#     }
#     output=""
#     for word in words:
#         output+=emojis.get(word,word)+ " "
#     return output

# user_in=input("=")
# print(emoji_converter(user_in))


#unpacking
# coordinators=(10,20,30)
# x,y,z=coordinators
# print(z)



decimal=int(input("Enter the number"))
binary_str=""
while decimal > 0:
    remainder= decimal%2
    binary_str=str(remainder) + binary_str
    decimal //=2
print(binary_str)













