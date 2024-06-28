# i=1
# while i<=5:
#     print("blah blah")
#     i+=1

# x=int(input("enter the number:"))
# y=1
# while y<=10:
#     print(x*y)
#     y+=1
    
    
        
# x=1
# while x <=10:
#     print([x**2])
#     x+=1
    

nums=(1,4,9,16,25,36,49,64,81,100)
# idx=1
# while idx < len(nums):
#     if nums[idx]==4:
#         print("number found on index" +str(idx))
#     idx+=1

def rotate(k,arr):
    sliced=arr[:k]
    join=arr[k:]+sliced
    return join

store=rotate(3,[1,2,3,4,5])
print(store)

# Define the list
my_list = ['a', 'b', 'c', 'd', 'r', 't', 'a', 'b', 'r', 't', 'f', 'g', 'h', 'j']

# Initialize an empty dictionary to store the counts
count_dict = {}

# Iterate over the list
for item in my_list:
    # If the item is already in the dictionary, increment its count
    if item in count_dict:
        count_dict[item] += 1
    # If the item is not in the dictionary, add it with count 1
    else:
        count_dict[item] = 1

# Print the result
print(count_dict)
