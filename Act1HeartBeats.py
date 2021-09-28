age = int(input("Enter your age: "))

max = -999999999
min = 999999999
theoricalMaxBeat = 220 - age
z3 = 0
z4 = 0
z5 = 0
numberActivities = 0

while True:

    bpm = int(input("Enter your bpm: "))
    if bpm == 0:
        break

    if bpm > theoricalMaxBeat * 0.9:
        z5 += 1
    elif bpm > theoricalMaxBeat * 0.8:
        z4 +=1
    elif bpm > theoricalMaxBeat * 0.7:
        z5 +=1
        

    if bpm > max:
        max = bpm
    if bpm < min:
        min = bpm

    numberActivities += 1
    

print("zona 3(>",theoricalMaxBeat * 0.7,") :", z3,"%")
print("zona 4(>",theoricalMaxBeat * 0.8,") :", z4,"%")
print("zona 5(>",theoricalMaxBeat * 0.9,") :", z5,"%")
print("max value ", max)
print("min value ", min)
