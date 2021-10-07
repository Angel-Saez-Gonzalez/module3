myList = [10,4,4,6,8,8,8,2,7]

newList = []
for item in myList:
    if item not in newList:
        newList.append(item)

print(myList)
print(newList)