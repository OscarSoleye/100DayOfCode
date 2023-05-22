total_bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
tip = int(input("What percentage tip would you like to give ? 10, 12, 15 ?"))
percentage_tip = (tip/100)*total_bill
total_bill_with_tips = percentage_tip + total_bill
split = int(input("How many people to split the bill?"))
split_per_person = round(total_bill_with_tips/split, 2)

print(f'Each person should pay : ${split_per_person}')