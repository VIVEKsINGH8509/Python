input_string = input("enter values separated by comma: ")
tuple_element = tuple(int(x) for x in input_string.split(','))
print(tuple_element)
sorted_tuple=tuple(sorted(tuple_element))

print(f'Sorted tuple in ascending order is : {sorted_tuple}')

threshold=int(input("enter a threshold value : "))

print(f'Tuple greater than specific threshold is : {sorted_tuple[threshold:]}')

