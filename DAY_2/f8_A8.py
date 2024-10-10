# Python program to display all the prime numbers within an interval
upper=int(input("your num :"))
prime_list = []
print("Prime numbers between", upper, "are:")

for num in range( upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime_list.append(num)

print(prime_list)