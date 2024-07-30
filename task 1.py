def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    
    for char in plaintext:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's neither, just add the character as it is (like spaces, punctuation)
        else:
            encrypted_text += char
            
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        # Check if character is an uppercase letter
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # If it's neither, just add the character as it is (like spaces, punctuation)
        else:
            decrypted_text += char
            
    return decrypted_text

while True:
    # Get user choice
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (Enter 'q' to quit): ").lower()
    
    if choice == 'e':
        plaintext = input("Enter the plaintext: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher_encrypt(plaintext, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        ciphertext = input("Enter the ciphertext: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        print("Decrypted text:", decrypted_text)
    elif choice == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
