# (weight(kg)/height(cm)2) * 10000

import numpy as np

def bmi(weight, height):
    bmi = (weight / height**2) * 10000
    bmi_final = round(bmi, 2)

    if bmi_final < 18.5:
        return f'{bmi_final} - niedowaga'
    if bmi_final > 18.5 and bmi_final <= 24.99:
        return f'{bmi_final} - prawidłowe bmi'
    if bmi_final > 25 and bmi_final <= 29.99:
        return f'{bmi_final} - nadwaga'
    if bmi_final > 30 and bmi_final <= 34.99:
        return f'{bmi_final} - otyłość I stopnia'
    if bmi_final > 35 and bmi_final <= 39.99:
        return f'{bmi_final} - otyłość II stopnia'
    if bmi_final >= 40:
        return f'{bmi_final} - otyłość III stopnia'
    
print(bmi(16.9, 105.4))
print(bmi(16.6, 99.1))
print(bmi(65, 182.88))
print(bmi(60, 160))
print(bmi(50, 180))
print(bmi(150, 160))
print(bmi(90, 160))


