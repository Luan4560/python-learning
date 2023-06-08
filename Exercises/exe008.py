# Write a script the reads a value in meters and convert to centimeters and milimeters

value = float(input('Type a value in meters: '))
print('The {} converted in KM is: {}'.format(value, value * 1000))
print('The {} converted in HM is: {}'.format(value, value * 100))
print('The {} converted in DAM is: {}'.format(value, value * 10))
print('The {} converted in M is: {}'.format(value, value * 1))
print('The {} converted in DM is: {}'.format(value, value * 0.1))
print('The {} converted in CM is: {}'.format(value, value * 0.01))
print('The {} converted in MM is: {}'.format(value, value * 0.001))
