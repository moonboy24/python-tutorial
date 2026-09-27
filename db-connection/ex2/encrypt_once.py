from password_utils import encrypt_password
from cryptography.fernet import Fernet 

# Generate key and save to file 

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key" , "wb") as f:
        f.write(key)
    print("Key saved to 'Secret Key'")
    
if __name__ == "__main__":
    # Uncomment this only this time 
    #generate_key()
    
    # Replace with your real MySQL root password
    
    encrypted = encrypt_password(input("Enter your SQL password: "))
    print("Encrypted password (Copy this to password_utils.py)")
    print(encrypted)