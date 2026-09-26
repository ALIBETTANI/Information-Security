# Information-Security
This is my first repositry that I will presented in my class with M Owais Wazir as my presentation partener.
<br>
This presentation was given by Dr. Hussain Shah Sahb.
<br>
One-Time Pad Encryption in Python
📘 Introduction
This project demonstrates One-Time Pad (OTP) encryption and decryption using Python. OTP is a classical cryptography technique that is theoretically unbreakable if the key is truly random and used only once.
.
🛠️ Implementation
Step 1: Define the Message
python
message = "HI"
•	Concept: String assignment
•	Role: Stores the plaintext message to encrypt.
Step 2: Convert Message to Binary
python
binary_message = ""
for c in message:
    binary_message += format(ord(c),'08b')
•	Concepts:
o	ord() → character → ASCII number
o	format(...,'08b') → decimal → 8-bit binary
•	Role: Converts plaintext into binary representation.
Step 3: Generate Random Binary Key
python
key = ""
for i in range(len(binary_message)):
    key += str(random.randint(0, 1))
•	Concepts:
o	random.randint() → generates random bits
o	len() → ensures key length matches plaintext
•	Role: Creates a random binary key.
Step 4: Encrypt (XOR)
python
cipher = ""
for m, k in zip(binary_message, key):
    cipher += str(int(m) ^ int(k))
•	Concepts:
o	zip() → pairs plaintext and key bits
o	XOR operation → reversible encryption
•	Role: Produces ciphertext.
Step 5: Decrypt (XOR Again)
python
decrypted_binary = ""
for i in range(len(cipher)):
    decrypted_binary += str(int(cipher[i]) ^ int(key[i]))
•	Concept: XOR reversibility
•	Role: Restores original binary plaintext.
Step 6: Convert Binary Back to Text
python
decrypted_message = ""
for i in range(0, len(decrypted_binary), 8):
    byte = decrypted_binary[i:i+8]
    decimal_value = int(byte, 2)
    decrypted_message += chr(decimal_value)
•	Concepts:
o	String slicing → chunks of 8 bits
o	int(...,2) → binary → decimal
o	chr() → decimal → character
•	Role: Converts binary back into the original message.
🖥️ Example Output
Code
----------Encryption------------
Plaintext    : 0100100001001001
Key          : 1010110010110101
Ciphertext   : 1110010011111100

----------Decryption------------
Ciphertext (Binary): 1110010011111100
Key (Binary):       1010110010110101
Plaintext (Binary): 0100100001001001
Original Message:   HI
<br>
Create a new file locally in VS Code

In your repo folder (Information-Security), create a new file called README.md or notes.md.

Paste the explanation (step-by-step breakdown we wrote earlier).

Stage and commit the file

bash
git add README.md
git commit -m "Add explanation file for OTP implementation"
Push to GitHub

bash
git push origin main


