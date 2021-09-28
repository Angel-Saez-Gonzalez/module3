capital = float(input("Input your capital: "))
interest = float(input("Input interest: "))
years = int(input("Input years: "))
n = 1
paidout = 0

while n <= years:
    quota = capital * ((interest/100 * pow(1 + interest/100, years)) / (pow(1 + interest/100, years) - 1))
    paidout += quota
    print()
    n += 1