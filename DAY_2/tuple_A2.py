input_string = input("enter name , age, city and country separated by comma")
tuple_element=tuple(str(x) for x in input_string.split(','))
print(tuple_element)

(name, age, city, country) = tuple_element

print(name)
print(age)
print(city)
print(country)