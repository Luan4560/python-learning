# Write a script that reas a salary of a staff
# ans show the new salary with 15% of increase;

currentSalary = float(input('Type your current salary: '))

result = currentSalary + (currentSalary * 15 / 100)

print('your new salary with 15% of increase is R${}'.format(result))
