from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

def generate_key():
    return get_random_bytes(16)  # AES-128 bit key

def encrypt_image(file_path, key):
    # Output file name (e.g., image.jpg.enc)
    output_path = file_path + ".enc"
    
    # Open image in binary read mode
    with open(file_path, 'rb') as f:
        image_data = f.read()
    
    # Initialize AES cipher
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Encrypt data (pad it first to fit block size)
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    
    # Write IV (Initialization Vector) + Encrypted Data
    with open(output_path, 'wb') as f:
        f.write(cipher.iv)
        f.write(encrypted_data)
    
    print(f"\n[SUCCESS] Image encrypted saved as: {output_path}")
    print("[INFO] You can try opening this file - it will be unreadable!")

def decrypt_image(file_path, key_hex):
    try:
        # Convert hex key string back to bytes
        key = bytes.fromhex(key_hex)
        
        # Determine output name (remove .enc extension)
        output_path = file_path.replace(".enc", "")
        if output_path == file_path:
            output_path = "decrypted_" + file_path

        with open(file_path, 'rb') as f:
            iv = f.read(16)  # Read the first 16 bytes (IV)
            encrypted_data = f.read()  # Read the rest
        
        # Initialize cipher with the same Key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt and unpad
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        
        # Write the original image back
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
            
        print(f"\n[SUCCESS] Image restored as: {output_path}")
        
    except ValueError:
        print("\n[ERROR] Incorrect Key or Corrupted Data!")
    except Exception as e:
        print(f"\n[ERROR] {e}")

def main():
    print("--- Image Encryption Tool ---")
    
    while True:
        print("\n" + "="*40)
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Exit")
        print("="*40)
        
        choice = input("Select Option: ")

        if choice == '3': break
        
        if choice == '1':
            file_path = input("Enter the full path of the image file (e.g., C:/Users/Name/Pictures/photo.jpg): ")
            
            if os.path.exists(file_path):
                key = generate_key()
                encrypt_image(file_path, key)
                print(f"\n[IMPORTANT] KEY (Save this to decrypt later!): {key.hex()}")
                
                # Optional: Delete original for security demo
                # os.remove(file_path) 
            else:
                print("File not found!")

        elif choice == '2':
            file_path = input("Enter the full path of the encrypted file (e.g., C:/Users/Name/Pictures/photo.jpg.enc): ")
            
            if os.path.exists(file_path):
                key_input = input("Enter the Key (Hex): ")
                decrypt_image(file_path, key_input)
            else:
                print("File not found!")

if __name__ == "__main__":
    main()
