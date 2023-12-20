def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) + key)
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr(ord(char) - key)
        decrypted_message += decrypted_char
    return decrypted_message

message = input("Enter your message: ")
key = int(input("Enter your encryption key: "))

encrypted_message = encrypt(message, key)
print("Encrypted message: ", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message: ", decrypted_message)
