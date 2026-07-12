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

# Count how many vowels are in a word

word = "programming"
vowels = "aeiou"

count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(count)    # 3


# Reverse a string manually

text = "Python"

reversed_text = ""

for letter in text:
    reversed_text = letter + reversed_text

print(reversed_text)

# Determine whether a number is even

number = 24

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Remove duplicate values

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)