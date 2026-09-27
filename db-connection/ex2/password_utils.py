
from cryptography.fernet import Fernet

# Class to prevent accidental print/log of password
class FakeStr(str):
    def __str__(self):
        return "****"
    def __repr__(self):
        return "****"

def load_key():
    return open("secret.key" , "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt the password and return a protected string

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)

def get_decrypted_password():
    encrypted_password = b'gAAAAABqluxaSmkYMbgpgeZ4ybc41RgKDukPwFhgduFkU6LE6pWVesb2lB05pq4lGQxsnnCYe9FcvfkFprW371i73Q42edwzBg=='
    return decrypt_password(encrypted_password)
