# Fernet module is imported from the
# cryptography package
from cryptography.fernet import Fernet


# key is generated
key = Fernet.generate_key()

print(key.decode())

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(b"welcome to geeksforgeeks")

# display the ciphertext
print(token.decode())

# decrypting the ciphertext
d = f.decrypt(token)

# display the plaintext and the decode() method
# converts it from byte to string
print(d.decode())
