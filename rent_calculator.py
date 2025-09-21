rent = int(input("Enter the rent amount: "))

food_cost = int(input("Enter the food cost(monthly): "))

electric_bill = int(input("Enter the electric bill(monthly): "))

unit_cost = int(input("Enter the unit cost of electricity: "))

preson = int(input("Enter the number of persons: "))

total_bill = electric_bill * unit_cost

monthly_expense = (rent + food_cost + total_bill)// preson

print("The monthly expense per person is: ", monthly_expense)