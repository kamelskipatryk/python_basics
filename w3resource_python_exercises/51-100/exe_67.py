# psi value = kPa value x 0.145038

kPa = float(input('Podaj wartość dla kilopascali: '))

psi = round(kPa * 0.145038, 4)
mmHg = round(kPa * 7.50062, 4)
atm_1 = 101.325 # in kilopascals
kpa_to_atm = round(kPa/atm_1, 4)

print(f'psi: {psi}')
print(f'mmHg: {mmHg}')
print(f'atm from kPa: {kpa_to_atm}')




