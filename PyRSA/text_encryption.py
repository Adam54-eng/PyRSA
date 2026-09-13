import pyrsa
from pyrsa import RSAKey

# ==========================================================
# Character dictionary (0 ↔ 94)
# ==========================================================

characters = (
    "0123456789"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

caractere_dict = {}

for i, char in enumerate(characters):
    caractere_dict[i] = char
    caractere_dict[char] = i

# ==========================================================
# Generate RSA keys
# ==========================================================

rsa = RSAKey(100, 500)
rsa.generate_encryption_key()
rsa.generate_decryption_key()

# ==========================================================
# Message to encrypt
# ==========================================================

text = "Hello PyRSA!"

encrypted = []

# Character → Number → Encryption
for char in text:
    value = caractere_dict[char]
    encrypted.append(rsa.modular_pow(rsa.e, value))

print("Original :", text)
print("Encrypted:", encrypted)

# ==========================================================
# Decryption
# ==========================================================

decrypted = ""

# Encrypted Number → Number → Character
for cipher in encrypted:
    value = rsa.modular_pow(rsa.d, cipher)
    decrypted += caractere_dict[value]

print("Decrypted:", decrypted)
