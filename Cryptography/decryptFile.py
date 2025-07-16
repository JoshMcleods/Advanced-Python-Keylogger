from cryptography.fernet import Fernet

# Load the encryption key with correct relative path
with open("Cryptography/encryption_key.txt", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# List of encrypted files with relative paths
encrypted_files = [
    "Keylogger/key_log.txt",
    "Keylogger/systeminfo.txt"
]

for encrypted_file in encrypted_files:
    with open(encrypted_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    # Save decrypted output to new files, e.g. prefix 'decrypted_'
    decrypted_filename = encrypted_file.replace(
        "Keylogger/", "Keylogger/decrypted_")

    with open(decrypted_filename, "wb") as f:
        f.write(decrypted_data)

    print(f"Decrypted {encrypted_file} → {decrypted_filename}")
