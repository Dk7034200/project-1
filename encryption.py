def caesar_cipher(text, mode='encrypt'):
    shift = 3  # setting as default value
    result = []

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + (shift if mode == 'encrypt' else -shift)) % 26)
            result.append(new_char)
        else:
          
            result.append(char)
    
    return ''.join(result)

def main():
    print("Encryption/Decryption")
    print("Choose any one:")
    print("1.Encrypt")
    print("2.Decrypt")
    
    try:
        mode_choice = int(input("Enter your choice (1 for encrypt, 2 for decrypt): "))
        
        if mode_choice == 1:
            mode = 'encrypt'
        elif mode_choice == 2:
            mode = 'decrypt'
        else:
            print("Invalid choice. Please enter 1 for encryption or 2 for decryption.")
            return
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")
        return

   
    text = input("Enter the message: ").strip()

    result = caesar_cipher(text, mode)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
