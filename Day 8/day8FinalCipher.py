from art.py import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-3: What happens if the user enters a number/symbol/space?
def caesar(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        print(f"The {direction}d text is {cipher_text}")
    elif direction == "decode":
        plain_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            plain_text += alphabet[new_position]
        print(f"The {direction}d text is {plain_text}")

# TODO-1: Import and print the logo from art.py when the program starts.

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. v

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
