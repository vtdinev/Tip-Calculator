print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill_with_tip = tip / 100 * total_bill + total_bill
person_pay = total_bill_with_tip / people
final = round(person_pay, 2)

print(final)
