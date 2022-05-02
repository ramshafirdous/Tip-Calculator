print("Welcome to the tip calculator!")

#Total Bill
bill= float(input("What was the total bill? $"))

#Percentage of tip
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))

#How many people to split the bill between
people= int(input("How many people to split the bill? "))

#Calculation and final output
amount= round( (bill/people) * (1+(tip/100) ) ,2)

print(f"Each peson should pay: ${amount}")

