from caesar_cipher import decrypt
from collections import Counter

most_common_letters = ['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u']


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
    most_occurred = max(freq_dict, key=freq_dict.get)

    top_10_possible_keys = []
    top_10_possible_texts = []
    for i in range(10):
        key = (ord(most_occurred) - ord(most_common_letters[i])) % 26
        top_10_possible_keys.append(key)
        result = decrypt(encoded_text, key)
        top_10_possible_texts.append(result)

    return top_10_possible_keys, top_10_possible_texts
