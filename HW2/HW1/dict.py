mydict = {}

mydict[0] = "underwear"
mydict[1] = "tank top"
mydict[2] = "jacket"

for key, value in mydict.items():
    print(f"Shopping item {key+1}: {value}")

print("You have", len(mydict), "items in the cart.")

while True:
    enter = input("\nWhat would you like to do [C]hange, [R]emove, [D]isplay, [S]earch? ")

    if enter.lower() == "c": 
        search = input("Enter item number to change: ")
        if search.isdigit():
            key = int(search) - 1
            if key in mydict:
                print(f"Found {mydict[key]} item")
                new_value = input("Enter new value: ")
                mydict[key] = new_value
            else:
                print("I'm sorry, not in the cart")
        else:
            print("Invalid key")

    elif enter.lower() == "r": 
        search = input("Enter item number to remove: ")
        if search.isdigit():
            key = int(search) - 1
            if key in mydict:
                removed = mydict.pop(key)
                print(f"The item {search} with value '{removed}' has been deleted")
            else:
                print("Item not found")
        else:
            print("Invalid key")

    elif enter.lower() == "d": 
        print("\nDisplaying Values")
        print("Item No   Value")
        for key, value in mydict.items():
            print(f"{key+1:<8} {value}")

    elif enter.lower() == "s": 
        item = input("Enter item number or name to search: ")
        found = False

        if item.isdigit():
            key = int(item) - 1
            if key in mydict:
                print(f"Found '{mydict[key]}' as item {key+1}")
                found = True
        else:
            for key, value in mydict.items():
                if value.lower() == item.lower():
                    print(f"Found '{value}' as item {key+1}")
                    found = True
                    break

        if not found:
            print("I'm sorry, not in the cart")

    elif enter == "*": 
        print("Bye!!")
        break

    else:
        print("Invalid option. Please choose again.")
