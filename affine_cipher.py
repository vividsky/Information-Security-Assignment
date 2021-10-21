def encrypt(text, key):
    """
    Encrypts a message using Affine cipher
    :param text: original message
    :param key: key used to encrypt the message
    :return: encrypted message
    """

    # y = (ax + b) % 26
    a = key[0]
    b = key[1]
    encrypted_string = ""
    for char in text:
        if ord(char) in range(97, 123):
            encrypted_string += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            encrypted_string += char
    return encrypted_string


def decrypt(text, key):
    """
    Decrypts a message encoded with Affine cipher
    :param text: encrypted message
    :param key: key used to encrypt the message
    :return: decrypted/decoded message
    """

    # y = ((a^-1)(x - b)) % 26

    a = key[0]
    b = key[1]
    a_inverse = 1   # default
    co_prime = True
    for i in range(1, 27):
        if i not in (1, a, 26) and a % i == 0 and 26 % i == 0:
            co_prime = False
            break
        if (a * i) % 26 == 1:
            a_inverse = i
    if not co_prime:
        return "Decryption not possible (modular multiplicative inverse of a doesn't exist)"

    decrypted_string = ""
    for char in text:
        if ord(char) in range(97, 123):
            decrypted_string += chr(((a_inverse * ((ord(char) - 97 - b) % 26)) % 26) + 97)
        else:
            decrypted_string += char
    return decrypted_string

    