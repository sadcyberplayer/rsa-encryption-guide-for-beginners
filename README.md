# 🔐 RSA Encryption & Decryption — Educational Guide

A beginner-friendly Python script that demonstrates how RSA Asymmetric Encryption works using the pycryptodome library. Built for students learning cybersecurity, ethical hacking, and cryptography.

---

## What is RSA?

RSA is an Asymmetric Encryption algorithm — meaning it uses two different keys:

- **Public Key:** Encrypts the data | Shared openly with anyone.
- **Private Key:** Decrypts the data | Kept secret by the receiver.

### The core idea:
- Anyone can encrypt a message using your Public Key.
- Only you can decrypt it using your Private Key.
- Even if an attacker intercepts the encrypted message — they can't read it without the Private Key.

---

## 📁 Project Structure

```
rsa-encryption-guide-for-beginners/
│
├── rsa_encryption_no_comments.py     ← encryption script — clean and simple
├── rsa_keys_generate_no_comments.py  ← key generation script — clean and simple
├── rsa_decryption_no_comments.py     ← decryption script — clean and simple
└── README.md                         ← this file
```

---

## Requirements

- Python 3.x
- pycryptodome library

Install the library:

```bash
pip install pycryptodome
```

If you get an import error, try installing `pycryptodomex` instead:

```bash
pip install pycryptodomex
```

Then change imports from `Cryptodome` to `Crypto` in the script.

## How to Run

```bash
python rsa_example.py
```

---

## 📜 The Script Guide

### Importing Libraries

We always have to import the Python libraries we need:

```python
# imports PKCS1_OAEP — the RSA encryption/decryption scheme
# OAEP adds random padding to the data before encrypting — makes it more secure
# Without OAEP, encrypting the same message twice gives the same cipher text — making it vulnerable
# to pattern analysis attacks. OAEP adds random padding before encrypting so every encryption
# output is different even for the same message.
from Cryptodome.Cipher import PKCS1_OAEP

# imports RSA — the algorithm used to generate and handle public/private keys
from Cryptodome.PublicKey import RSA
```

---

### Key Generation — Generating RSA Keys

```python
# RSA.generate(2048) = generate two keys using 2048 bits — longer = more secure
pairkeys = RSA.generate(2048)

# export_key() converts the key object into raw bytes so it can be saved or printed
private_key = pairkeys.export_key()

# public_key() gets only the public key from the pair then export_key() converts it to bytes
public_key = pairkeys.public_key().export_key()

# print both keys to screen
print(private_key)
print(public_key)
```

---

### Encryption — Encrypting Using the Public Key

```python
# the public key stored as raw bytes
# this is the key the sender uses to ENCRYPT the data
# \n = new line inside the key format (PEM format)
public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjAN...\n-----END PUBLIC KEY-----'

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
```

---

### Decryption — Decrypting Using the Private Key

```python
# the encrypted bytes we want to decrypt
# this is the cipher text — the output of the encryption above
encrypted_data = b'I\x0f\x17!\x8d\xe6...'

# the private key stored as raw bytes
# this is the key the RECEIVER uses to DECRYPT the data
# only the owner of the private key can decrypt what was encrypted with the public key
private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEow...\n-----END RSA PRIVATE KEY-----'

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
```

---

## ⚠️ Important Security Notes

- Never hardcode keys in your source code — if someone sees your code they have your keys.
- Never share your Private Key — ever.
- Always use 2048-bit or higher for RSA keys in real applications.
- This script is for educational purposes only.

---

## 📚 Related Topics to Learn Next

- AES Symmetric Encryption.
- Hashing (MD5, SHA1, SHA256).
- SSL/TLS — how HTTPS uses RSA.
- Digital Signatures.
- Man-in-the-Middle Attacks.

---

Thanks for reading! 😊
