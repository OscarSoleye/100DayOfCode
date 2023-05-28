import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ['rock', 'paper', 'scissors']
symbol = [rock, paper, scissors]
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.").lower()

random_option = options[random.randint(0, 2)]


if user_input in options:
    if random_option == options[0]:
        print(rock)
    elif random_option == options[1]:
        print(paper)
    elif random_option == options[2]:
        print(scissors)

    if user_input == options[0]:
        print(rock)
    elif user_input == options[1]:
        print(paper)
    elif user_input == options[2]:
        print(scissors)

    if user_input == random_option:
        print("You Draw")
    elif user_input == options[0] and random_option == options[1]:
        print("You Lose")
    elif user_input == options[1] and random_option == options[2]:
        print("You Lose")
    elif user_input == options[2] and random_option == options[1]:
        print("You Win")
    elif user_input == options[1] and random_option == options[0]:
        print("You Win")
    elif user_input == options[0] and random_option == options[2]:
        print("You Win")
else:
    print("You lose")
