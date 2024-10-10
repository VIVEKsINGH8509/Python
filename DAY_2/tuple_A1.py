my_list=[]
n=int(input("ENTER the no. of elements to be added in the list: "))

for i in range (0, n):
    num = int(input("Enter element: "))
    my_list.append(num)


print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:-1])
print(my_tuple[0:-1:2])  #(0 1 2 3 4 5 6 67 78 )
print(my_tuple[::-1])
