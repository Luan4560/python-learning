# Write a script that ask the KM traveled for a rent car an
# quantity of days of rent. Calculate the price to be paid
# Knowing that value cost is R$60 per day and 0.15 for KM traveled

km = float(input('What is the traveled KM?: '))
day = int(input('What were rent car days?: '))

valuePerDay = day * 60
valuePerKm = km * 0.15

totalValue = valuePerDay + valuePerKm

print('The total cost is : R${:.2f}'.format(totalValue))
