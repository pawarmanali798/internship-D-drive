# random_list=[[1,2,3],[4,5],[6]]
# for value in range(random_list):
#     print(random_list)


# random_list=[[1,2,3],[4,5],[6,7,8,9]]
# new_list=[value for array in random_list for value in array if value%2==0]
# print(new_list)


def is_prime(value):
    return True

print([ele for ele in range(30,40) if is_prime(ele)])


people = [
    {"name": "Alice", "friend_list": ["Bob", "Charlie"], "age": 30, "location": {"city": "New York", "country": "USA"}},
    {"name": "Bob", "friend_list": ["Alice", "David"], "age": 25, "location": {"city": "London", "country": "UK"}},
    {"name": "Charlie", "friend_list": ["Alice", "Emily"], "age": 28, "location": {"city": "Paris", "country": "France"}},
    {"name": "David", "friend_list": ["Bob", "Emily"], "age": 32, "location": {"city": "Berlin", "country": "Germany"}},
    {"name": "Emily", "friend_list": ["Charlie", "David"], "age": 27, "location": {"city": "Madrid", "country": "Spain"}},
]


dictionary=[dict for dict in people if "Alice" in dict["friend_list"] and dict["location"]["city"]=="Paris"]
print(dictionary)






