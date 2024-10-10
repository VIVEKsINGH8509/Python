test_list = [1, 2, 3, 4, 5]
position = int(input("Enter the position from where the list needs to be rotated: "))

size = len(test_list)
print(size)
position %= size
print(position)
print(str(test_list))

test_list = test_list[position+1:] + test_list[:position + 1]
print(str(test_list))