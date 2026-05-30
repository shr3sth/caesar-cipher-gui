def caesar_cipher(text, shift):

    result = ""

    for char in text:

        if char.isalpha():

            base = ord('a') if char.islower() else ord('A')

            shifted = chr((ord(char) - base + shift) % 26 + base)

            result += shifted

        else:
            result += char

    return result   


text = input("Enter the text to encrypt/decrypt: ")
shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
result = caesar_cipher(text, shift)
print("Result:", result)
