# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def draw(self):
#         print("called draw function")

#     def move(self):

#         print("Moving the point")

# point1=Point(11,20)
# print(point1.x)
# point1.draw()

# class Information:
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName

#     def talk(self):
#         print(f"invoke talk method {self.firstName}")

# obj1=Information("manali","pawar")
# print(obj1.firstName)
# obj1.talk()

class Info:
    def func(self):
        print("This is function 1")

obj1=Info()
obj1.func()

import time

def func1():
    result=time.sleep(3)
    return "hi"

store=func1()
print(store)
