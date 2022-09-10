operation = input("What operation do you want to perform: ")

if operation == "plus":
    first_value = input("enter first value: ")
    second_value = input("enter second value: ")

    total = int(first_value) + int(second_value)

    print (total)

elif operation == "minus":
    first_value = input("enter first value: ")
    second_value = input ("enter second value: ")

    total = int(first_value) - int(second_value)

    print (total)

elif operation == "division":
    first_value = input("enter first value: ")
    second_value = input ("enter second value: ")

    total = int(first_value) // int(second_value)

    print (total)

elif operation == "multiple":
    first_value = input("enter first value: ")
    second_value = input("enter second value")
    
    total = int(first_value) * int(second_value)

    print (total)

