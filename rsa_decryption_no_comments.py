from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

encrypted_data = b'...'

private_key = b'-----BEGIN RSA PRIVATE KEY-----...-----END RSA PRIVATE KEY-----'
private_key_new = RSA.import_key(private_key)
DecFunction = PKCS1_OAEP.new(private_key_new)


clear_data = DecFunction.decrypt(encrypted_data)
print(clear_data)
