print("Welcome to Python Pizza Parlor!")
size = input("What size pizza do you want ? S, M or L ?")
add_pepperoni = input("Do you want pepperoni ? Y or N")
extra_cheese = input("Do you want extra cheese ? Y or N")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25


if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or "L":
        bill += 3


if extra_cheese == "Y":
    bill += 3

print(f"Your bill is : ${bill}")