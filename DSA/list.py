my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)


array = [ 9, 4, 8, 14, 24, 5, 12, 15]

miniVal = array[0]

for i in array:
  if i < miniVal:
    miniVal = i

print("lowest value: ", miniVal)


# Find the largest number in a list

numbers = [12, 5, 87, 34, 19]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)   # 87