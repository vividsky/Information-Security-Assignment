from affine_cipher import decrypt
from collections import Counter

most_common_letters = ['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u']


def calculate_key(x1, y1, x2, y2):
    """
    Calculates the value of a and b that will be used to decrypt affine cipher
    :param x1: Possible letter #1 in plaintext (before encoding)
    :param y1: Most occurred letter #1 in the encoded text (after encoding)
    :param x2: Possible letter #2 in plaintext (before encoding)
    :param y2: Most occurred letter #2 in the encoded text
    :return: Value of a and b (key)
    """
    x1 = ord(x1) - 97
    y1 = ord(y1) - 97
    x2 = ord(x2) - 97
    y2 = ord(y2) - 97

    if x1 > x2:
        x_diff = x1 - x2
        y_diff = (y1 - y2) % 26
    else:
        x_diff = x2 - x1
        y_diff = (y2 - y1) % 26

    y = y_diff
    count = 0
    while True:
        if y % x_diff == 0:
            a = y // x_diff
            b = (y1 - x1*a) % 26
            return [a, b]
        y += 26
        count += 1
        if count > 1000:
            return [1, 1]


def letter_frequency_attack(encoded_text):
    """
    Performs letter frequency attack on th encrypted text
    :param encoded_text: encrypted text
    :return: Top 10 possible original texts
    """
    freq_dict = Counter(encoded_text)
    for el in (' ', ',', '.', '/', '-'):
        if el in freq_dict:
            del (freq_dict[el])

    freq_list = [(k, v) for k, v in freq_dict.items()]
    freq_list.sort(key=lambda x: (x[0], -x[1]))

    if len(freq_list) < 2:
        return [], []
    most_occurred_1 = freq_list[0][0]
    most_occurred_2 = freq_list[1][0]

    top_10_possible_keys = []
    top_10_possible_texts = []
    for i in range(10):
        key = calculate_key(most_common_letters[i], most_occurred_1, most_common_letters[i+1], most_occurred_2)
        top_10_possible_keys.append(key)
        result = decrypt(encoded_text, key)
        top_10_possible_texts.append(result)

    return top_10_possible_keys, top_10_possible_texts

