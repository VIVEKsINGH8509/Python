accBalance = int(input("enter your acc. balance : "))

if accBalance == 0:
    print("insufficient Balance")



while True:
    withdrawalAmount = int(input("Enter the amount to be withdrawl : "))
    if withdrawalAmount % 10 != 0:
        print("Amount must be a multiple of 10.")
    elif withdrawalAmount > accBalance:
        print("insufficient Balance")
    elif withdrawalAmount <= accBalance:
        accBalance -= withdrawalAmount
        print(f'remaining balance {accBalance}')
    ask = input("Type 'y' to continue & 'n' to exit.")
    if ask == 'n':
        break