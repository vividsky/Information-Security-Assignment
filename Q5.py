import math


def create_inverse_key_matrix(key: str) -> list[list[int]]:
    """
    Creates matrix inverse (if possible)
    :param key: 2X2 key matrix
    :return: 2X2 inverse matrix
    """
    key_matrix = create_key_matrix(key)
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[1][0] * key_matrix[0][1]) % 26
    if det < 0:
        det += 26
    det_inverse = -1
    for i in range(1, 26):
        if (det * i) % 26 == 1:
            if math.gcd(i, 26) == 1:
                det_inverse = i
    if det_inverse == -1:
        print("Decryption is not possible")
        return []
    for i in range(2):
        for j in range(2):
            if i != 1 or j != 1:
                if (i+j) % 2 != 0:
                    key_matrix[i][j] = - key_matrix[i][j] + 26
                else:
                    temp = key_matrix[i + 1][j + 1]
                    key_matrix[i + 1][j + 1] = key_matrix[i][j]
                    key_matrix[i][j] = temp
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = (key_matrix[i][j] * det_inverse) % 26
    return key_matrix


def create_key_matrix(key: str) -> list[list[int]]:
    """
    Creates a 2X2 matrix from the key string
    :param key: key string used to encrypt the message
    :return: 2X2 matrix of given key string
    """
    key_matrix = [[0] * 2 for _ in range(2)]
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[k]) - 97
            k += 1
    return key_matrix


def encrypt_column(key_matrix: list[list[int]], column: list[list[int]]) -> list[list[int]]:
    """
    Multiplies a single column with the key_matrix
    :param key_matrix: 2X2 matrix
    :param column: 2X1 column made up of two letters from the text
    :return: 2X1 encrypted column
    """
    encrypted_column = [[0] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            encrypted_column[i][0] += key_matrix[i][j] * column[j][0]
        encrypted_column[i][0] = encrypted_column[i][0] % 26
    return encrypted_column


def matrix_to_string(encrypted: list[list[int]]) -> str:
    """
        Creates encrypted string from encrypted matrix
        :param encrypted: encrypted matrix of the form 2XM
        :return: encrypted string
        """
    encrypted_string = ""
    for i in range(len(encrypted[0])):
        for j in range(len(encrypted)):
            encrypted_string += chr(encrypted[j][i] + 97)
    return encrypted_string


def encrypted_message(text: str, key: str, conversion_type: str = "e") -> str:
    """
    Encrypts a message using Hill cipher
    :param text: original message
    :param key: key used to encrypt the message
    :param conversion_type: e/E for encryption, d/D for decryption (Default: e)
    :return: encrypted message
    """
    encrypted_matrix = [[] for _ in range(2)]
    if conversion_type in ('d', 'D'):
        key_matrix = create_inverse_key_matrix(key)
        if not key_matrix:
            return "Non-Invertible-Matrix (please choose a different key)"
    else:
        key_matrix = create_key_matrix(key)

    text += 'x' * (len(text) % 2)
    
    for i in range(0, len(text) - 1, 2):
        column = [[0] for _ in range(2)]
        for j in range(2):
            column[j][0] = ord(text[j + i]) - 97
        
        encrypted_column = encrypt_column(key_matrix, column)
        
        encrypted_matrix[0].append(encrypted_column[0][0])
        encrypted_matrix[1].append(encrypted_column[1][0])
    
    encrypted_string = matrix_to_string(encrypted_matrix)
    return encrypted_string


def main():
    """
    Code execution starts here
    :return: None
    """
    print("2X2 HILL CIPHER")
    inp_text = input("Enter text: ")
    inp_key = input("Enter key: ")
    conversion_type = input("Enter type (e for encryption / d for decryption): ")

    # Encrypting letters only
    text = ""
    for el in inp_text.lower():
        if ord(el) in range(97, 123):
            text += el

    key = ""
    for el in inp_key.lower():
        if ord(el) in range(97, 123):
            key += el
    # to ensure 4 letter key
    key = (key + 'axfg')[:4]
    result = encrypted_message(text, key, conversion_type)
    print("Original message: ", text)
    print("Decrypted message:" if conversion_type in ('d', 'D') else "Encrypted message:", result)


if __name__ == "__main__":
    main()
