from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

pairkeys = RSA.generate(2048)

private_key = pairkeys.export_key()
public_key = pairkeys.public_key().export_key()

print(private_key)
print(public_key)