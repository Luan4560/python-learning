# Write a script that converts reais to dolar
# cotation is USD1,00 = R$4.92;

valueDolar = float(input('Type the value that you want to convert: '))

print('R${} = US${:.2f}'.format(valueDolar, valueDolar / 4.92))
