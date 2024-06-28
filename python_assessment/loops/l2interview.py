myList=['a','b','c','d','a','b','c','t','r','s','x']

dictCount={}
count=0
for item in myList:
    if item not in dictCount:
        dictCount[item] = 1
    else:
        dictCount[item] += 1

print(dictCount)

