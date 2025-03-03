# Problem Set 1 A
# Name: Rafael Ederli
# Time Spend: 0:25

# Part A: Saving for a House
yearly_salary = float(input("Enter the starting yearly salary: "))
monthly_salary = yearly_salary / 12
portion_saved = float(input("Enter the portion of salary to be saved, in decimal: "))
monthly_contribution = monthly_salary * portion_saved

cost_of_dream_home = float(input("Enter the cost of dream home: "))
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment

amount = 0

r = 0.05 / 12 # Return on investiment

months = 0

while amount < down_payment:
    amount = amount * (1 + r) + monthly_contribution
    months = months + 1
print(months)