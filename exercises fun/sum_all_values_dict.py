incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
     total_income += value  # Accumulate the values in total_income

print(total_income)