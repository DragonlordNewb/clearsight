import pyaes

def encrypt(plaintext, key):
    # Key must be bytes, so we convert it
    key = key.encode("utf-8")

    aes = pyaes.AESModeOfOperationCTR(key)
    return aes.encrypt(plaintext)

def decrypt(ciphertext, key):
    aes = pyaes.AESModeOfOperationCTR(key)

    # Decrypted data is always binary, decode to plaintext
    return aes.decrypt(ciphertext).decode("utf-8")
