from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

public_key = b'-----BEGIN PUBLIC KEY-----.....----END PUBLIC KEY-----'
public_key_new = RSA.import_key(public_key)

data = "Hello, World!".encode("ascii")

EncFunction = PKCS1_OAEP.new(public_key_new)
encrypted_data = EncFunction.encrypt(data)


print(encrypted_data)
