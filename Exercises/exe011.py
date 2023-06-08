# Write a script that calculate area of width and heigth of a wall 
# and the ink quantity needed to paint all wall, 
# keep in mind that 1lt of ink paints an area fo 2m².

width = float(input('Type the width of the wall: '))
height = float(input('Type the height of the wall: '))

area =  height * width;

print('{}m²'.format(area))
print('LT of ink needed to pait all wall: {}lt'.format(area / 2 ))