import caesar_cipher
import affine_cipher
import freq_attack_caesar
import freq_attack_affine
import hill_cipher


def main():
    """
    Code execution starts here.
    :return: None
    """
    menu = """\nMenu: 
    1. CAESAR CIPHER
    2. AFFINE CIPHER
    3. LETTER FREQUENCY ATTACK ON CAESAR CIPHER
    4. LETTER FREQUENCY ATTACK ON AFFINE CIPHER
    5. HILL CIPHER
    0. EXIT
    Enter Choice: """

    conversion_type_string = '''\nChoose conversion type:
    0. Encryption
    1. Decryption
    Enter Choice: '''
    
    choice = 1
    conversion_type = 0
    while choice != 0:
        print("\n****************************************************************************")
        print(menu, end="")
        choice = int(input().strip())
        if choice in (1, 2, 5):
            print(conversion_type_string, end="")
            conversion_type = int(input().strip())
        
        if choice == 1:
            print("\n-------------------------------CAESAR CIPHER--------------------------------")
            inp_text = input('Enter text: ')
            text = inp_text.lower()
            try:
                key = int(input('Enter integer key: '))
            except ValueError:
                print("Please enter integer key.")
                continue

            print()
            print("Original text: ", text)
            print('Result:', caesar_cipher.encrypt(text, key) if conversion_type == 0
                  else caesar_cipher.decrypt(text, key))
        
        elif choice == 2:
            print("\n-------------------------------AFFINE CIPHER--------------------------------")
            inp_text = input("Enter text: ")
            text = inp_text.lower()
            try:
                key = list(map(int, input("Enter space-separated key values (a and b): ").split()))
            except ValueError:
                print('Please enter integer keys')
                continue

            print()
            print("\nOriginal text:", text)
            print('Result:', affine_cipher.encrypt(text, key) if conversion_type == 0
                  else affine_cipher.decrypt(text, key))
        
        elif choice == 3:
            print("\n------------------LETTER FREQUENCY ATTACK ON CAESAR CIPHER------------------")
            inp_text = input('Enter the encrypted text: ')
            enc_text = inp_text.lower()
            print("\nTop 10 possible key and plaintext pairs:\n")
            possible_original_key, possible_original_text = freq_attack_caesar.letter_frequency_attack(enc_text)
            for i in range(10):
                print(f'{i+1}.\tPossible original key: {possible_original_key[i]}\n'
                      f'\tPossible original text: {possible_original_text[i]}')
        
        elif choice == 4:
            print("\n------------------LETTER FREQUENCY ATTACK ON AFFINE CIPHER------------------")
            inp_text = input('Enter the encrypted text: ')
            enc_text = inp_text.lower()
            possible_original_key, possible_original_text = freq_attack_affine.letter_frequency_attack(enc_text)
            if not possible_original_text:
                print("Please enter long enough text to perform letter frequency attack.")
                continue
            print("\nTop 10 possible key and plaintext pairs:\n")
            for i in range(10):
                print(f'{i+1}.\tPossible key: a = {possible_original_key[i][0]}, b = {possible_original_key[i][1]}\n'
                      f'\tPossible original text: {possible_original_text[i]}')
        
        elif choice == 5:
            print("\n--------------------------------HILL CIPHER---------------------------------")
            inp_text = input("Enter text: ")
            inp_key = input("Enter string key: ")
            print()
            hill_cipher.result(inp_text, inp_key, conversion_type)
        
        elif choice == 0:
            print("Exit")
            break
        else:
            print("\nPlease enter valid input.")


if __name__ == "__main__":
    main()
