# Image Encryption Tool (AES)

This is a simple image encryption and decryption tool implemented in Python using AES (Advanced Encryption Standard). The tool allows users to encrypt image files so that they become unreadable and later restore them using the correct secret key. It is designed for educational purposes to demonstrate how encryption can be applied to protect multimedia data.

## 💻 Working Demo

https://github.com/user-attachments/assets/ebf0339c-7fb0-4e74-9318-05e24d6144e7

## Features

- **AES Image Encryption**: Encrypts image files using AES-128 in CBC mode.
- **Secure Key Generation**: Automatically generates a random 128-bit encryption key.
- **IV Handling**: Uses a unique Initialization Vector (IV) for each encryption.
- **File-Based Encryption**: Encrypted images are saved with a `.enc` extension.
- **Safe Decryption**: Restores the original image only when the correct key is provided.
- **Menu-Driven CLI**: Simple and interactive command-line interface.

## Prerequisites

- Python 3.x
- `pycryptodome` library

## Installation

### Step 1: Install Required Libraries

```bash
pip install pycryptodome
```

### Step 2: Download or Clone the Repository

```bash
git clone https://github.com/NehaamKhan/Image-Cryptography-Tool.git
```

### Step 3: Navigate to the Project Directory

```bash
cd Image-Cryptography-Tool
```

## Usage

### Step 1: Run the Script

```bash
python image_encryption.py
```

### Step 2: Choose an Option

```
1. Encrypt an Image
2. Decrypt an Image
3. Exit
```

### Step 3: Encrypt an Image

- Enter the full path of the image file.
- The program will:
  - Encrypt the image
  - Save it as `image_name.ext.enc`
  - Display a secret key (hex)

⚠️ **Save the key securely** — it is required for decryption.

### Step 4: Decrypt an Image

- Enter the full path of the encrypted `.enc` file.
- Provide the correct hexadecimal key.
- The original image will be restored.

### Step 5: Exit

Select option `3` to safely exit the program.

## Notes

- AES is used in **CBC mode** with **PKCS7 padding**.
- The encrypted image file will be unreadable and cannot be opened normally.
- If an incorrect key is used, decryption will fail.
- This project is intended **for educational and demonstration purposes only**.

## License

This project is licensed under the [MIT License](LICENSE).
