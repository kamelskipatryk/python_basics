import math

arr = [34,55,7,8,90,734]
first = math.inf
second = math.inf

for i in range(0, len(arr)):
    if arr[i] < first:
        first = arr[i]

for i in range(0, len(arr)):
    if arr[i] != first and arr[i] < second:
        second = arr[i]

print(second)


