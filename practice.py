import numpy as np

my_list = [10, 12, 15, 18, 22, 27, 30]

print(type(my_list))

two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(two_d_list)

my_array_numb = np.array(my_list)
my_array_numb2 = np.array(my_list, dtype=float)

print(my_array_numb)
print(my_array_numb2)

array_to_list = my_array_numb.tolist()
print(array_to_list)