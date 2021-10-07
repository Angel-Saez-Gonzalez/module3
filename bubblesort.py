myList = [10,4,8,2,7]

for index in range(len(myList)):
    for num in range(len(myList)-index-1):
        if myList[num] > myList[num+1]:
            myList[num], myList[num+1] = myList[num+1], myList[num]

print(myList)