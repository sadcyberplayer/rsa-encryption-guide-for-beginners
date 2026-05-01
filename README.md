

## 🔐 RSA Encryption & Decryption — Educational Guide
# A beginner-friendly Python script that demonstrates how RSA Asymmetric Encryption works using the pycryptodome library. Built for students learning cybersecurity, ethical hacking, and cryptography.

### What is RSA?
## RSA is an Asymmetric Encryption algorithm — meaning it uses two different keys:

# Public Key: Encrypts the data | Shared openly with anyone .
# Private Key:  Decrypts the data | Kept secret by the receiver.

## The core idea:
# Anyone can encrypt a message using your Public Key.
# Only you can decrypt it using your Private Key.
# Even if an attacker intercepts the encrypted message — they can't read it without the Private Key.

## 📁 Project Structure
rsa-encryption-guide-for-beginners/
│
├── rsa_encryption_no_comments.py     ← encryption script — clean and simple
├── rsa_keys_generate_no_comments.py  ← key generation script — clean and simple
├── rsa_decryption_no_comments.py     ← decryption script — clean and simple
└── README.md                         ← this file

------------

## Requirements
- Python 3.x
- pycryptodome library

# Install the library:
pip install pycryptodome

# If you get an import error, try installing `pycryptodomex` instead:
pip install pycryptodomex
# Then change imports from `Cryptodome` to `Crypto` in the script.

## How to Run:
python rsa_example.py

------------
########## THE SCRIPT GUIDE:

# Firstly, We always have to import the python libraries we need:
# imports PKCS1_OAEP — the RSA encryption/decryption scheme
# OAEP adds random padding to the data before encrypting — makes it more secure
# Without OAEP, encrypting the same message twice gives the same cipher text — making it vulnerable to pattern analysis attacks. OAEP adds random padding before encrypting so every encryption output is different even for the same message.
from Cryptodome.Cipher import PKCS1_OAEP

# imports RSA — the algorithm used to generate and handle public/private keys
from Cryptodome.PublicKey import RSA


# ---- KEY GENERATION | In this part we generate RSA keys ----

# RSA.generate(2048) = generate two keys using 2048 bits — longer = more secure
pairkeys = RSA.generate(2048)

# export_key() converts the key object into raw bytes so it can be saved or printed
private_key = pairkeys.export_key()

# public_key() gets only the public key from the pair then export_key() converts it to bytes
public_key = pairkeys.public_key().export_key()

# print both keys to screen
print(private_key)
print(public_key)

# ---- END OF KEY GENERATION ----


# ---- ENCRYPTION | Here we will start to encrypt using the public key ----

# the public key stored as raw bytes
# this is the key the sender uses to ENCRYPT the data
# \n = new line inside the key format (PEM format)
public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsQfSiVuLukdduVRss8qY\nfTVxV+qG39SvIFAWbi3lF58Jb4n9mQ/9s8Ds/IhWD1Z5mrVn6rKECphGSNLiVpt8\nNOdzlm/EH4Uj8Xjke9HHM25jAfYjFPOD4JpRJ3y5WnFwl6FMwXkQLlfua51pyL2n\nEPd8z1gGgO6GHdisKdGdPRo0MM7vc1Mnwo3vQ+ky1h3brxzx0xvjF/lBLUXvrpCx\nAAFu5tizVN7QCRZFt2ywhpVPqXi5ChRWrr68QOSWHeJ/VEMkFDRMEv0oKdgTiSiQ\nugI6Sgba4gILjlkaQbOMV12F1oo6tZ2OLsQTv8KgFS9qN7J22JOJ8uV9Ua2MU6I7\nlwIDAQAB\n-----END PUBLIC KEY-----'

# import_key() converts the raw bytes back into an RSA key object that Python can use
public_key_new = RSA.import_key(public_key)

# the plain text message we want to encrypt
# .encode("ascii") converts the string into bytes — RSA needs bytes not strings
data = "Hello, World!".encode("ascii")

# create a new OAEP encryption function using the public key
# PKCS1_OAEP.new() = prepare the RSA encryptor with our public key
EncFunction = PKCS1_OAEP.new(public_key_new)

# encrypt the data using the public key
# result is raw encrypted bytes (cipher text) — looks like random garbage
encrypted_data = EncFunction.encrypt(data)

# print the encrypted result to screen
print(encrypted_data)

# ---- END OF ENCRYPTION ----


# ---- DECRYPTION | Here will decrypt the data using the private key ----

# the encrypted bytes we want to decrypt
# this is the cipher text — the output of the encryption above
encrypted_data = b'I\x0f\x17!\x8d\xe6\x06\xceUI+\x94\xe7\xb2\xc3Z\xf7\xff\xeeD\xfcl\xbe@\x89\xfa\x9e \xef7\xa2\xed\x7f,;N\x18\x94P\x97\xf32A\x81Z`\x8b|\xf0\x84\x81J\x9d\xa4Qk%\xc8\xe4\x03\x1cF\x9b#\xb5\x0cv\xd6\x00\xcfI\xfa\xb0\xd1\xf1\xde\x01/\xdb\xf2\xa6\xe5"\x93a\xad\xcdpY\xdb\x97d\x1a\xfcV\xd1T\xe9\xcc^\x19\xbf\x19\x9c^\xf8l!h\x1eM\x14\x91\x15\x86\xc8\x8bA\xe3_\xaf\xde5~>\x181|\x1a\x1fl?\x94\x0f\xea2\x93{g\x89#<\x16P\x12\\1X\x11z\xe6\x16\xd5L\x84\x96\xfd\x18\x17jn\x89i\xbe\xa5/\xeb\x82\x8f\x0fW\xfc\xfd\xe4&\x9d\xce=\xc5\x17\xb9\xceIff$\x02$\xc8Z(\x8e\xc4\xc7\xeb\xe7\x08q\x0cR&\xfd\xdd#\x9fbB\xb7\xc10\x13\xb1.\xf1\xfa\x8c\xf7\xf6\xb4A\xfd\xd4m\xe3Y<t\'\xfa\xa1<\xc1g\xa2zT\xc3\x10v\x99\xa6\x1aS\x83\xe8J\x8e\xddl\xea\xd3\x83\xd58\xe7\x96'

# the private key stored as raw bytes
# this is the key the RECEIVER uses to DECRYPT the data
# only the owner of the private key can decrypt what was encrypted with the public key
private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAsQfSiVuLukdduVRss8qYfTVxV+qG39SvIFAWbi3lF58Jb4n9\nmQ/9s8Ds/IhWD1Z5mrVn6rKECphGSNLiVpt8NOdzlm/EH4Uj8Xjke9HHM25jAfYj\nFPOD4JpRJ3y5WnFwl6FMwXkQLlfua51pyL2nEPd8z1gGgO6GHdisKdGdPRo0MM7v\nc1Mnwo3vQ+ky1h3brxzx0xvjF/lBLUXvrpCxAAFu5tizVN7QCRZFt2ywhpVPqXi5\nChRWrr68QOSWHeJ/VEMkFDRMEv0oKdgTiSiQugI6Sgba4gILjlkaQbOMV12F1oo6\ntZ2OLsQTv8KgFS9qN7J22JOJ8uV9Ua2MU6I7lwIDAQABAoIBAACTwPOiW8XuCPfb\nYZtYdBTRwXPYQjulQDOVGe2esq+Csjot3f4gwjf9eghSEs3BVMDUtJOxpKKQNTJ0\nQDlTZR1FtT0ZUi9eyhY1ybDppyzwwDE3xzeAmmkiDP+u9WppEkU8SQ7HFplqv06U\ngyLHaNhc+4gwMPKR/y1GZpFLAKiRVZPABSKlvnE6c5vApiI9w3z6ZsM65FbX/MgJ\nWknxLm+/rwByqv+2pnNLEVwPpGSn2VUcU1a3dND+RvrnaFs33hQxif1+YYbiN9De\nyMha66/X410/6Gq/xRUpIfVAFmghqD+nhNA9BQWaEfMDeSYPIpNBd0NAY+djh6c2\nr/fVDVkCgYEAxK7gaOmYmcYX0WGkOUl+PBWT7Pzsa7ln1TPCLt4y0cBpDqBf8NuJ\n4rYUoeuoUqdq5x/8oKHE8eGVwx7mFCsGD2KQoj8g7Y/cjqWYh2cZ6nJ4DS8Pi2rQ\nMAQm6/r0VESRG2g1vOfK/oYSxswteeRjSKSVrTr2m2vYRid9crQqa7sCgYEA5mum\nYDJo+XOaQZVH6Bu5G7c4p9MBQV75tW5fBSdEQfpb+Eeqi7OpZgDpsZ6irJdjIkuX\ng2PDX3hhUS2CyeKeLZMahi+wTJ9jp8nRvEpZroy92KwDSq9IbJi3B+Bzv5lPwR8i\nAknUPwoHtEoj7nBbi71lps8m7f5YP3WpSuwfu9UCgYAKZhiVU2xvDOsrddch9EHJ\nWXa1u/WgCHB19EObCMJ1FpA3ZsFL0b+rjebvXK9Ml29uguFveL4Z78xkQZj2jgPH\nAnYVLfNGvCl0HUtANXJIU/8G62sN+vrA3ydTqLQMVIe7hDn7H+I6rMoHWro4zJt3\nNsR3ITvyobQQmXvneaEYiwKBgQDPbwQVv+v+/dJVzkUwsJyBVf28H9oWdqEIc3c5\nVXM+jltzdVkUcUZEHPhFPdGm3JaTTkf1Mb+119KMWRNQGiJaVv7e5FmrcSYu7CJT\nhv+bgvp578j62De0A/tqLOcnCqbg7d0ZAEwCAE6VQNV+F0piz7uOYxjh0kKxxoQE\nffPHjQKBgGzAmd0TGYvTFTy8rh/POvbWTCz+Fw5E+1oeJKELuYLoNnAG+hiVY9Dx\noe9TgYg05kuHBgHqiSzmcMV8V9ie+1n7OPGQliNeD9OayqPWMvJYOQCsw4fhR/Mn\nUSBbf91UbjBFxLogG0Gp5xWkwqeiCmjCdkEzcB20llKtHU09ODJg\n-----END RSA PRIVATE KEY-----'

# import_key() converts the raw private key bytes into an RSA key object Python can use
private_key_new = RSA.import_key(private_key)

# create a new OAEP decryption function using the private key
# same PKCS1_OAEP.new() but this time we pass the PRIVATE key for decryption
DecFunction = PKCS1_OAEP.new(private_key_new)

# decrypt the encrypted data using the private key
# reverses the encryption and gives back the original plain text bytes
clear_data = DecFunction.decrypt(encrypted_data)

# print the decrypted result — should print: b'Hello, World!'
print(clear_data)

# ---- END OF DECRYPTION ----


## Important Security Notes
    # Never hardcode keys in your source code — if someone sees your code they have your keys.
    # Never share your Private Key — ever.
    # Always use 2048-bit or higher for RSA keys in real applications.
    # This script is for educational purposes only.

## Related Topics to Learn Next
    # AES Symmetric Encryption.
    # Hashing (MD5, SHA1, SHA256).
    # SSL/TLS — how HTTPS uses RSA.
    # Digital Signatures.
    # Man-in-the-Middle Attacks.

# Thanks for reading! :)