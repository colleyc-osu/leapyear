rpt = 1

while rpt == 1:
	rpt = 0
	user_input = input("Please enter your year: ")

	try:
		n = int(user_input)
	except:
		rpt = 1
		print("Wrong input. Try again.")

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
