print("Hello! Welcome to tip calculator!")
bill = float(input("How much is your bill?\n"))
tip_percentage = int(input("How much percentrage you'd like to give? 15, 20 or 25?\n"))/100
people = float(input("How many people is sharing the bill?\n"))
total_bill=bill*(1+tip_percentage)
#split = round(total_bill/people)
split = "{:.2f}".format(total_bill/people)
print(f"Each person should pay ${split}.")
