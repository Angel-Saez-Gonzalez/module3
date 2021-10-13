list = []

while True:
    print("1.- Add a number to the list")
    print("2.- Add a number in a position in the list")
    print("3.- Show the length of the list")
    print("4.- Delete the last number in the list")
    print("5.- Delete a number in the list")
    print("6.- Count numbers")
    print("7.- Positions of a numbers")
    print("8.- Show the list")
    print("9.- Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        num = int(input("Input a number: "))
        list.append(num)
    
    elif option == 2:
        num = int(input("Input a numer: "))
        pos = int(input("Input the position: "))
        if pos <= len(list):
            list.insert(pos, num)
        else:
            print("end of index")

    elif option == 3:
        print("The length of the list is ",len(list))

    elif option == 4:
        if len(list) > 0:
            print("te last position is ", list.pop())
    
    elif option == 5:
        pos = int(input("Input the position: "))
        if pos <= len(list):
            print("Deleting te position ", pos ,list.pop(pos))
    
    elif option == 6:
        num = int(input("Input a numer: "))
        print("The ocurrences of numer ", num, " is ", list.count(num))

    elif option == 7:
        num = int(input("Input a numer: "))
        index = 1
        for elem in list:
            if elem == num:
                print("")
            index += 1
        list.index()

    elif option == 8:
        for elem in list:
            print(elem, end=" ")
            print()

    elif option == 9:
        break
