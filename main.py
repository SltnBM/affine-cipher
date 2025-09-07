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
    print("\nEncryption Process:")
    for ch in plaintext:
        if ch.isupper():
            x = ord(ch) - ord('A')
            y = (a * x + b) % 26
            print(f"{ch} -> ({a}*{x} + {b}) mod 26 = {y} -> {chr(y + ord('A'))}")
            ciphertext += chr(y + ord('A'))
        elif ch.islower():
            x = ord(ch) - ord('a')
            y = (a * x + b) % 26
            print(f"{ch} -> ({a}*{x} + {b}) mod 26 = {y} -> {chr(y + ord('a'))}")
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
    print("\nDecryption Process:")
    for ch in ciphertext:
        if ch.isupper():
            y = ord(ch) - ord('A')
            x = (a_inv * (y - b)) % 26
            print(f"{ch} -> {a_inv}*({y} - {b}) mod 26 = {x} -> {chr(x + ord('A'))}")
            plaintext += chr(x + ord('A'))
        elif ch.islower():
            y = ord(ch) - ord('a')
            x = (a_inv * (y - b)) % 26
            print(f"{ch} -> {a_inv}*({y} - {b}) mod 26 = {x} -> {chr(x + ord('a'))}")
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
        print("\nCiphertext:", ciphertext)

        decrypted = decrypt_affine(ciphertext, a, b)
        print("\nDecrypted :", decrypted)
    except ValueError as e:
        print("Error:", e)
