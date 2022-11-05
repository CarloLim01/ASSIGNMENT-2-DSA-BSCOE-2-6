# Write a python program that do the following:
# - Display the initial content of the array.
# - Display a menu of options.
# - Allow user to select item in the menu (check if valid).
# - Perform the selected option (you may prompt additional info to user when need).
# - Display the resulting values of the array.

# (\033[1;35;1m  \033[0m)

import time

Array = [3, 8, 9, 0, 11, 20, 24, 30, 69, 71]
time.sleep(1)
print("\033[1;37;1m>>> WELCOME <<<\033[0m\n")
time.sleep(2)
print(f"Array: \033[1;35;1m{Array}\033[0m")
print("Index Array: \033[1;35;1m[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\033[0m\n")
print("Menu: Pick A number")
print("\t\033[1;35;1m1\033[0m → Add an element")
print("\t\033[1;35;1m2\033[0m → Insert an element")
print("\t\033[1;35;1m3\033[0m → Modify an element")
print("\t\033[1;35;1m4\033[0m → Delete an elementt")
print("\t\033[1;35;1m5\033[0m → Arrange in ascending order")
print("\t\033[1;35;1m6\033[0m → Arrange in descending order")
print()

time.sleep(3)
AskUser = int(input("\033[1;3mWhat do you want to do? (1-6):\033[0m  "))
def start():
    if AskUser == 1:
        time.sleep(1)
        Number = int(input("\n\033[1;3mWhat Number that you want to add:\033[0m  "))
        Add = Array.append(Number)
        time.sleep(2)
        print("\n\033[1;35;1mThe Number you want has been Added\033[0m")
        return Add

    elif AskUser == 2:
        time.sleep(1)
        Number2 = int(input("\n\033[1;3mWhat Number that you want to insert:\033[0m  "))
        time.sleep(1)
        Number3 = int(input("\n\033[1;3mWhere do you want to insert the number?\033[0m  "))
        Add1 = Array.insert(Number3, Number2)
        time.sleep(2)
        print("\n\033[1;35;1mThe element has been Insert\033[0m")
        return Add1
    
    elif AskUser == 3:
        time.sleep(1)
        Number4 = int(input("\n\033[1;3mWhat index position do you want to Modify:\033[0m  "))
        time.sleep(1)
        Number5 = int(input("\n\033[1;3mWhat Number do want to add:\033[0m  "))
        Add2 = Array.pop(Number4)
        Array.insert(Number4, Number5)
        time.sleep(2)
        print("\n\033[1;35;1mThe element has been Modify\033[0m")
        return Add2

    elif AskUser == 4:
        time.sleep(2)
        Number_5 = int(input("\n\033[1;3mType the Number that you want to Delete:\033[0m  "))
        Add3 = Array.remove(Number_5)
        return Add3

    elif AskUser == 5:
        Add4 = Array.sort()
        time.sleep(2)
        print("\n\033[1;35;1mThe element has been arrange to ascending order\033[0m")
        return Add4

    elif AskUser == 6:
        Add5 = Array.reverse()
        time.sleep(2)
        print("\n\033[1;35;1mThe element has been arrange to descending order\033[0m")
        return Add5

start()
print()
time.sleep(2)
print(f"The New Array: \033[1;35;1m{Array}\033[0m\n\n")
time.sleep(2)
print("\033[1;37;1m>>> THANKYOU <<<\033[0m")

