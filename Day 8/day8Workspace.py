# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("What is your name ?")
    print("How old are you ?")
    print("How do you do ?")

greet()

def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How old are you, {name} ?")
    print(f"How do you do ?")

greet_with_name("Wale")


def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Waleda", "Aberdeen")