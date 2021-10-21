def encrypt(plain_text: str, key: int) -> str:
    """
    Encrypts a message using Caesar cipher
    :param plain_text: original message
    :param key: key used to encrypt the message
    :return: encrypted message
    """
    encoded_text = []
    for letter in plain_text:
        if ord(letter) in range(97, 123):
            encoded_text.append(chr((ord(letter)-97 + key) % 26 + 97))
        else:
            encoded_text.append(letter)
    return ''.join(encoded_text)


def decrypt(encoded_text: str, key: int) -> str:
    """
    Decrypts a message encoded with Caesar cipher
    :param encoded_text: encrypted message
    :param key: key used to encrypt the message
    :return: decrypted/decoded message
    """
    plain_text = []
    for letter in encoded_text:
        if ord(letter) in range(97, 123):
            plain_text.append(chr((ord(letter)-97 - key) % 26 + 97))
        else:
            plain_text.append(letter)
    return ''.join(plain_text)
