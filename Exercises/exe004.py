# Write a script that reads somenthing on keyboard and print your primitive type
# and all possible informations about it.

info = input('Type something:');

print(type(info))
print('isdigit ->', info.isdigit()) 
print('isalfaNum ->',info.isalnum())
print('isalpha ->', info.isalpha())
print('isascii ->', info.isascii())
print('isdecimal ->', info.isdecimal())
print('isidentifier ->', info.isidentifier())
print('islower ->', info.islower())
print('isupper ->', info.isupper())
print('isprintable ->', info.isprintable())
print('isspace ->', info.isspace())
print('istitle ->', info.istitle())
