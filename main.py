from math import gcd

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def encrypt_affine(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' is not valid! It must be coprime with 26.")

    ciphertext = ""
    for ch in plaintext:
        if ch.isupper():
            x = ord(ch) - ord('A')
            y = (a * x + b) % 26
            ciphertext += chr(y + ord('A'))
        elif ch.islower():
            x = ord(ch) - ord('a')
            y = (a * x + b) % 26
            ciphertext += chr(y + ord('a'))
        else:
            ciphertext += ch
    return ciphertext


def decrypt_affine(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' is not valid! It must be coprime with 26.")

    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse not found.")

    plaintext = ""
    for ch in ciphertext:
        if ch.isupper():
            y = ord(ch) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        elif ch.islower():
            y = ord(ch) - ord('a')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('a'))
        else:
            plaintext += ch
    return plaintext



if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    a = int(input("Enter key 'a': "))
    b = int(input("Enter key 'b': "))

    try:
        ciphertext = encrypt_affine(plaintext, a, b)
        print("Ciphertext:", ciphertext)

        decrypted = decrypt_affine(ciphertext, a, b)
        print("Decrypted :", decrypted)
    except ValueError as e:
        print("Error:", e)