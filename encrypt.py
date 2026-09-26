# Encryption using OTP and Exclusive OR algorithm

message = input("Enter message: ")
key = input("Enter 08 bits binary key: ")

# Convert key from binary string to integer
key_value = int(key, 2)

plaintext_text = ""
ciphertext_text = ""

# Process each character
for ch in message:

    # Convert character into ASCII value
    value = ord(ch)

    # Convert ASCII value into 8-bit binary
    binary_value = format(value, "08b")

    # Add plaintext binary
    plaintext_text += binary_value

    # XOR
    ciphertext = value ^ key_value

    # Convert encrypted value into 8-bit binary
    encrypted_binary = format(ciphertext, "08b")

    # Add ciphertext binary
    ciphertext_text += encrypted_binary
print("--------------------------------")
print("Plaintext  :", plaintext_text)
print("Key        :", key)
print("Ciphertext :", ciphertext_text)
print("--------------------------------")
#decryption
plaintext_text=ciphertext^key_value
original_message=str(plaintext_text)
print("plaintext   :",plaintext_text)
print("Original message :",original_message)