def encrypt_message(message, key):
    alphabet = "abcdefghigklmnopqrstuvwxyz"
    encrypted = ""

    for letter in message:
        letter_index_position = (alphabet.index(letter) + key) % 26
        encrypted += alphabet[letter_index_position]

    return encrypted


def decrypt_message(message, key):
    alphabet = "abcdefghigklmnopqrstuvwxyz"
    encrypted = ""

    for letter in message:
        letter_index_position = (alphabet.index(letter) - key) % 26
        encrypted += alphabet[letter_index_position]

    return encrypted


print(encrypt_message("xyz", 2))

print(1 % 26)