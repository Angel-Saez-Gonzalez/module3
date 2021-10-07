myList = [10,4,4,6,8,8,8,2,7]

print(myList)

for index in range(len(myList)//2):
    myList[index], myList[len(myList)-index - 1] = myList[len(myList)-index - 1], myList[index]

print(myList)
