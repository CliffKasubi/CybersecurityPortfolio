# === Secret Message Encoder/Decoder (with spaces & punctuation) ===

def encode_message(message, key):
    encoded = ""
    for char in message:
        if char.isalpha():  # Only letters are shifted
            shift = key % 26
            if char.islower():
                encoded += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encoded += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encoded += char  # Keep spaces and punctuation as-is
    return encoded

def decode_message(encoded_message, key):
    return encode_message(encoded_message, -key)

# Main program
print("=== Secret Message Encoder/Decoder ===")
choice = input("Type 'E' to encode or 'D' to decode: ").upper()
text = input("Enter your message: ")
key = int(input("Enter the secret key (number): "))

if choice == 'E':
    result = encode_message(text, key)
    print("\nEncoded message:", result)
elif choice == 'D':
    result = decode_message(text, key)
    print("\nDecoded message:", result)
else:
    print("Invalid choice. Type 'E' to encode or 'D' to decode.")