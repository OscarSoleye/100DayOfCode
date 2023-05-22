import random

random_side = random.randint(0, 1)  # Use 0 and 1 so that will be the range of random numbers available to the user
if random_side == 1:
    print("Heads")
else:
    print("Tails")