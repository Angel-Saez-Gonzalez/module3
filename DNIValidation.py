letters = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:

    dni = input("Input your DNI: ")
    digits = dni[:-1]    
    letter = dni[-1].upper()
    
    if len(dni) != 9 and digits.isdigit():
        digits = int(dni[:-1])
        break
    else:
        print("Format incorrect")

resultDivision = digits % 23

print(resultDivision) 

if letters[resultDivision] == letter:
    print("Correct")
else:
    print("Incorrect")
