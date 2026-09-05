def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            # Shift and wrap around using % 26
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char # keep spaces, numbers, symbols same
    return result

def decrypt(text, shift):
    # Decrypting is just encrypting with negative shift
    return encrypt(text, -shift)

def main():
    print("--- Caesar Cipher Tool ---")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose option (1/2/3): ")

        if choice == '3':
            print("Bye!")
            break

        if choice not in ['1', '2']:
            print("Invalid choice!")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
        except ValueError:
            print("Shift must be a number!")
            continue

        if choice == '1':
            encrypted = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted}")1
        else:
            decrypted = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()