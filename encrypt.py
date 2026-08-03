def encrypt(message, shift):
    encrypted_message = ""
    
    for letter in message:
        if letter.isupper():
            letter_position = ord(letter) - ord('A')
            shifted_position = (letter_position + shift) % 26
            encrypted_message += chr(shifted_position + ord('A'))
        
        elif letter.islower():
            
            letter_position = ord(letter) - ord('a')
            shifted_position = (letter_position + shift) % 26
            encrypted_message += chr(shifted_position + ord('a'))
        
        else:
            
            encrypted_message += letter
    
    return encrypted_message


def decrypt(message, shift):

    return encrypt_message(message, -shift)


def show_menu():
    print("\n===== CAESAR CIPHER =====")
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("3. Exit")


def main():
    while True:
        show_menu()
        user_choice = input("What would you like to do? ")

        if user_choice == "1":
            message = input("Type your message: ")
            shift = int(input("Choose a shift value (e.g. 3): "))
            print("Your encrypted message is:", encrypt(message, shift))

        elif user_choice == "2":
            message = input("Type the encrypted message: ")
            shift = int(input("What shift value was used? "))
            print("Your decrypted message is:", decrypt(message, shift))

        elif user_choice == "3":
            print("Thanks for using Caesar Cipher! Goodbye.")
            break

        else:
            print("Hmm, that's not a valid option. Try again.")


main()