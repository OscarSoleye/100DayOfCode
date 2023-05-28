# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random

# Write your code below this line 👇
print(names)
randomName = random.choice(names)
print(f'{randomName} is going to buy the meal today!')

# Alternatively you can create a variable that holds the size of the list

listSize = len(names) - 1
nameIndex = random.randint(0, listSize)
randomName = names[nameIndex]

print(f'{randomName} is going to buy the meal today!')