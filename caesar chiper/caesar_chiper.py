alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher (start_text, shift_amount, cip_direction):
    end_text = ""
    if cip_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabeth:    
            position = alphabeth.index(char)
            new_position = position + shift_amount
            end_text += alphabeth[new_position]
        else: 
            end_text += char
    
    print(f"Your {cip_direction}d text is : {end_text}")


from ascii import logo
print(logo)

conti = True
while conti:
    print("Welcome to Caesar Cipher Text!")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 

    caesar_cipher(start_text=text, shift_amount=shift, cip_direction=direction)
    goal = input('Type "yes" to continue, or "no" to finish\n')
    if goal == "no":
        conti = False
        print("So long, then... Goodbye!")