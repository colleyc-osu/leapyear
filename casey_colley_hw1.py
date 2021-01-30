n = int(input("Please enter your year: "))

if (n % 100 == 0):
    if (n % 400 == 0):
        print(str(n) + " is a leap year.")
    else:
        print(str(n) + " is not a leap year.")
else:
    if (n % 4 == 0):
        print(str(n) + " is a leap year.")
    else:
        print(str(n) + " is not a leap year.")
