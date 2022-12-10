#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to this super awesome tip calcualtor! ")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip_dec = int(tip) / 100
amount_per_person = round((float(bill) / int(people)) * (1+tip_dec), 2)
amount_per_person_f = "{:.2f}".format(amount_per_person) # formats to include 2 decimal points to show trailing zero


print(f"Each person should pay: ${amount_per_person_f}")