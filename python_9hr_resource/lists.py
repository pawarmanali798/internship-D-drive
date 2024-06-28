users=["leo","don","snow"]
data=["23","true","don"]

emptyList=[]

print("don" in users)
print("")

print("leo" in emptyList)
print("")

print(users[0])
print("") #leo

print(users[-3:-1])
print("")

print(users.index('don'))
print("") #1

print(len(data))
users.append("Elsa")
print(users)

users+=["John"]
print(users)

users.extend("manali")#puts each separate letter as elements in list i.e.'m','a','n','a','l','i'
print(users)


new_users=["manali","neha"]
new_users.extend(["shivani"])
print(new_users)

users.insert(0,"snow")
print(users)

users[2:2]=["ruby"]
print(users)

colors=["white","blue","green","orange","yellow","grey","brown","black"]
colors[2:4]=["red","magenta"] #values passed as index here delete the existed ele from 2-4 and then extends the list for new provided elem
print(colors)

colors.remove("blue")
print(colors)

print(colors.pop())
print(colors)

del colors[3]
print(colors)

# del colors
# print(colors)