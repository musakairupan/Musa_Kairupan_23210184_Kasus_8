def encrypt(text, k):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + k) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result
def decrypt(text, k):
    return encrypt(text, -k)
if __name__ == "__main__":
    print("Program Caesar Cipher")
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    shift = int(input("Masukkan jumlah pergeseran (k): "))
    encrypted = encrypt(plaintext, shift)
    decrypted = decrypt(encrypted, shift)
    print("Teks terenkripsi:", encrypted)
    print("Teks terdekripsi:", decrypted)