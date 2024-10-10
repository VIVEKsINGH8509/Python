to_do_list = []

while True:
    print("1. to add element to the list")
    print("2. to remove element from the list")
    print("3. to view the list")
    print("4. sort array in asc")

    num = int(input("What you wanna do?!!"))
    match num:
        case 1:
            to_do_list.append(input(""))
            print(to_do_list)
        case 2:
            rem = input("What you wanna remove: ")
            to_do_list.remove(rem)
            print(to_do_list)
        case 3:
            print(to_do_list)
        case 4:
            num=[]
            while True:
               num_to_be_sorted=(input("no. to be taken"))
               if num_to_be_sorted == 'e':
                   break
               else:
                num.append(num_to_be_sorted)



