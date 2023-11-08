import day8sezarlogo

print(day8sezarlogo.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(user_text, shift_value, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_value *= -1
    else:
        shift_value = shift_value
    for i in user_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            if new_position > 51:
                end_text += alphabet[new_position - 52]
            else:
                end_text += alphabet[new_position]
        else:
            end_text += i
    print(f"The Chiper Direction is:{cipher_direction} adn Text is {end_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(user_text=text, shift_value=shift, cipher_direction=direction)
    response = input("type yes if you wont to go again.Otherwise type no: ")
    if response == "yes":
        continue
    elif response == "no":
        print("Goodbye")
        break
    else:
        print("please enter a valid response")
