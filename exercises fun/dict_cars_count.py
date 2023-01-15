dictCars = {0: {
  'brand': 'Ford',
  'electric': False,
  'year': 1964,
  'colors': 'red'
},
1: {
  'brand': 'BMW',
  'electric': False,
  'year': 1978,
  'colors': 'white'
},
2: {
  'brand': 'Toyota',
  'electric': True,
  'year': 1990,
  'colors': 'blue'
},
3: {
  'brand': 'Toyota',
  'electric': False,
  'year': 1922,
  'colors': 'black'
},
4: {
  'brand': 'Honda',
  'electric': True,
  'year': 2002,
  'colors': 'yellow'
},
5: {
  'brand': 'BMW',
  'electric': True,
  'year': 2020,
  'colors': 'red'
},
6: {
  'brand': 'Buggati',
  'electric': False,
  'year': 2033,
  'colors': 'red'
}}

# showing all data
print("\nShowing all data:\n")
for cID, cInfo in dictCars.items():
    print (cID, cInfo)

# iterate through a Nested dictionary
print("\nIterate through a nested dictionary:")
for cID, cInfo in dictCars.items():
    print("\nCar ID:", cID)
    for key in cInfo:
        print(key + ':', cInfo[key])

# All data we want from dict
print("\nAll data we want from dict:")
cBMW = 0
cElectric = 0
c2000 = 0

for cID, cInfo in dictCars.items():
    for key in cInfo:
        # BMw's
        if key == 'brand' and cInfo[key] == 'BMW':
            cBMW += 1
        # electrics
        if key == 'electric' and cInfo[key] == True:
            cElectric += 1
        # cars above 2000'
        if key == 'year' and cInfo[key] > 2000:
            c2000 += 1
            
print("How many BMW's in data:", cBMW)
print("electrics:", cElectric)
print("Cars above 2000 year:", c2000)