# White a script that read two note of an student, and show the average;

noteOne = float(input('Note 1: '))
noteTwo = float(input('Note 2: '))

print('The average between note1: {} and note2: {} is {:.1f}'.format(
    noteOne, noteTwo, (noteOne + noteTwo) / 2))
