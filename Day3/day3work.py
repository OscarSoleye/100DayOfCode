print("Welcome to the Wavy Wale Wave Ride!!")
height = int(input("How tall are you in cm?"))
bill = 0

if height >= 120:
    print("You're tall enough")
    age = int(input("How old are you ?"))
    if age < 12:
        bill = 5
        print("It'll cost $5")
    elif age <= 18:
        bill = 7
        print("It'll cost $7")
    else:
        bill = 12
        print("It'll cost $12")
    wants_photo = input("Do you want a photo taken ? Y or N")
    if wants_photo == "Y" or "y":
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("Sorry you're not tall enough :(")

