print("Welcome to my Love Calculator")
name1 = input("What is your name ? ").lower()
name2 = input("What is their name ? ").lower()

countT = name1.count("t") + name2.count("t")
countR = name1.count("r") + name2.count("r")
countU = name1.count("u") + name2.count("u")
countE = name1.count("e") + name2.count("e")
countL = name1.count("l") + name2.count("l")
countO = name1.count("o") + name2.count("o")
countV = name1.count("v") + name2.count("v")
countE = name1.count("e") + name2.count("e")

sumTrue = str(countT + countR + countU + countE)
sumLove = str(countL + countO + countV + countE)

percentage = int(sumTrue + sumLove)


print(percentage)

if percentage <= 10 or percentage >= 90 :
    print(f"Your score is {percentage}, you go together like coke and mentos")
elif percentage >= 40 and  percentage <= 50 :
    print(f"Your score is {percentage}, you're alright together")
else:
    print(f"Your Score is {percentage}%")






