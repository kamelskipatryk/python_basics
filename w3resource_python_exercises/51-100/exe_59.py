
def convert_height():
    pass

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
 
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
 
print(f'Your height is : {h_cm} cm.')



