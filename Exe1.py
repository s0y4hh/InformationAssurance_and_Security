import hashlib
import base64
from datetime import datetime

class ISS_Lab:
    '''
    A class to simulate the Information Security Systems Lab.
    It contains methods to view, encrypt, decrypt, calculate hash, verify integrity, backup, and restore data.
    
    '''
    def __init__(self):
        self.data = "Very Secure Information"
    
    def view_data(self):
        return "Current Data: " + self.data
    
    def encrypt_data(self, key):
        encrypted_data = "".join([chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(self.data)])
        return base64.b64encode(encrypted_data.encode()).decode()
    
    def decrypt_data(self, key, encrypted_data):
        decrypted_data = base64.b64decode(encrypted_data).decode()
        return "".join([chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(decrypted_data)])
    
    def calculate_hash(self):
        return hashlib.sha256(self.data.encode()).hexdigest()
    
    def verify_integrity(self, hash_value):
        return "Valid" if self.calculate_hash() == hash_value else "Invalid"
    
    def backup_data(self):
        with open("backup.txt", "w") as file:
            file.write(self.data)
    
    def restore_data(self):
        with open("backup.txt", "r") as file:
            self.data = file.read()
        return self.data

def run_lab():
    """
    Run the ISS Lab application, providing a menu for various operations.
    """
    encrypted_data = None
    hash_value = None
    lab = ISS_Lab()
    while True:

        print(f"""
              
Current Encrypted Data: {encrypted_data}
Current Hash Value: {hash_value}

1. View Current Data
2. Encrypt Data
3. Decrypt Data
4. Calculate Hash
5. Verify Integrity
6. Backup Data
7. Restore Data
8. Exit
""")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        
        # Use match-case for better readability and structure
        match choice:
            case 1:
                # View current data
                print(lab.view_data())
            case 2:
                # Encrypt data with a given key
                key = input("Enter the encryption key: ")
                encrypted_data = lab.encrypt_data(key)
                print("Encrypted Data: ", encrypted_data) 
            case 3:
                try:
                    # Decrypt data with a given key
                    key = input("Enter the decryption key: ")
                    EncryptedData = encrypted_data
                    if lab.decrypt_data(key, EncryptedData) == lab.data:
                        print("\nSuccefully Decrypted Data:", lab.decrypt_data(key, EncryptedData))
                        encrypted_data = None
                    else:
                        print("Data is not decrypted correctly")
                except Exception as e:
                    print("Error decrypting data or the key is wrong", e)
            case 4:
                # Calculate and display the hash of the current data
                hash_value = lab.calculate_hash()
                print("Hash Value:", hash_value)
            case 5:
                # Verify the integrity of the data by comparing hash values
                hash = input("Enter the hash value to verify: ")
                print("Integrity Check:", lab.verify_integrity(hash))
                if lab.verify_integrity(hash) == "Invalid":
                    print("Data has been tampered.")
                else:
                    print("Data is secure.")
                    hash_value = None
            case 6:
                # Backup the current data and save the timestamp
                lab.backup_data()
            case 7:
                # Restore data from the backup file
                try:
                    print("Data Restored:", lab.restore_data())
                except FileNotFoundError:
                    print("No backup file found.")
            case 8:
                # Exit the application
                break
            case _:
                # Handle invalid choices
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    run_lab()