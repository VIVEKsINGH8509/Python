input_string = input("enter values separated by comma: ")
tuple_element = tuple(int(x) for x in input_string.split(','))
print(tuple_element)

sum=0
for i in tuple_element:
    sum += i
print(f"The sum of given tuple is: {sum}")

print(f"the avg of given tuple is: {sum/ len(tuple_element)}")

print(f"the max and min values are : {max(tuple_element)} & {min(tuple_element)}")

print(f"The no. of elements in tuple are: {len(tuple_element)}")

