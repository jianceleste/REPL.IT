import numpy as np

def checkIfRightTriangle(num1, num2, num3):
    a = np.sqrt(num1**2 + num2**2)  # a will be the hypotenuse
    if a == num3: return print('This triangle IS a right triangle!')
    else: return print('This triangle IS NOT a right triangle!')


loop = True
while loop:
    try:
        hypotenuse = int(input('Value of the hypotenuse: '))
        adjacent = int(input('Value of the adjacent: '))
        opposite = int(input('Value of the opposite: '))

        checkIfRightTriangle(adjacent, opposite, hypotenuse)

        tryAgain = input('\nWould you like to try again? <y/n> ')
        if tryAgain.lower() == 'y': loop = True
        else: loop = False

    except ValueError or TypeError:
        print('Invalid input! Please try again.\n')
        loop = True
