
def convert_feet(feet):
    inches = feet * 12
    yards = feet * 0.333333
    miles = feet * 0.000189394
    meters = feet * 0.3048
    return f'{feet} feet are:\nInches: {inches} \nYards: {yards} \nMiles: {miles}\nMeters: {meters}\n'



print(convert_feet(1))
print(convert_feet(56))
print(convert_feet(25))




