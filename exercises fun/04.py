from math import pi

def calculate(val):
    a = pi * (val**2)
    return a

while True:
    print('\nTo exit type: end')
    r = input('Enter the radius of the circle: ')
    if r == 'end': break
    try:
        val = int(r)
        print('The area of the circle is:', calculate(val))
        continue
    except ValueError:
        try:
            val = float(r)
            print('The area of the circle is:', calculate(val))
            continue
        except ValueError:
            print("You entered the wrong value. Please enter a number.")