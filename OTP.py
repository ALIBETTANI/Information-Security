import random

# Step 1: Define the message
message = "HI"
print("----------Encryption------------")
# Step 2: Convert message to binary (8 bits per character)
#binary_message = ''.join(format(ord(c), '08b') for c in message)
#start with empty string
binary_message=""
for c in message:
    binary_message+=format(ord(c),'08b')
print("plaintext    :", binary_message)

# Step 3: Generate random binary key of same length
key = ""
for i in range(len(binary_message)):
    bit = random.randint(0, 1)   # random 0 or 1
    key += str(bit)
print("Key      :", key)

# Step 4: Encrypt (XOR each bit of message with key)
cipher = ""
for m, k in zip(binary_message, key):
    cipher += str(int(m) ^ int(k))
print("Ciphertext   :", cipher)
print("\n----------Decryption------------")
# Step 5: Decrypt (XOR cipher with same key)
decrypted_binary = ""
for i in range(len(cipher)):
    decrypted_binary += str(int(cipher[i]) ^ int(key[i]))

# Step 6: Convert binary back to text
decrypted_message = ""
for i in range(0, len(decrypted_binary), 8):
    byte = decrypted_binary[i:i+8]          # take 8 bits
    decimal_value = int(byte, 2)            # binary → decimal
    decrypted_message += chr(decimal_value) # decimal → character
print("Ciphertext (Binary):", cipher)
print("Key (Binary):       ", key)
print("Plaintext (Binary): ", decrypted_binary)
print("Original Message:   ", decrypted_message)