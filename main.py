import CaesarCipher, Q3, Q4, AffineCipher, HillCipher
def main():
    menu = """\nChoose Options: 
    1. CAESAR CIPHER
    2. AFFINE CIPHER
    3. LETTER FREQUENCY ATTACK ON CAESAR CIPHER
    4. LETTER FREQUENCY ATTACK ON AFFINE CIPHER
    5. HILL CIPHER
    0. EXIT
    Enter Choice: """
    
    choice = 1
    while choice != 0 :
        print("\n****************************************************")
        print(menu)
        choice = int(input().strip())
        
        if choice == 1:
            print("******************CAESAR CIPHER*******************")
            inp_text = input('Enter text: ')
            text = inp_text.lower()
            key = int(input('Enter Integer key: '))

            print("\n")
            print("Original text", text)
            print('Encrypted text:', CaesarCipher.encrypt(text, key))
            print('Decrypted text:', CaesarCipher.decrypt(CaesarCipher.encrypt(text, key), key))
        
        elif choice == 2:
            print("******************AFFINE CIPHER*******************")
            inp_text = input("Enter text: ")
            text = inp_text.lower()
            key = list(map(int, input("Enter space-separated Integer a and b: ").split()))

            print("\n")
            print("\nOriginal text:", text)
            print("Encrypted text:", AffineCipher.encrypt(text, key))
            print("Decrypted text:", AffineCipher.decrypt(AffineCipher.encrypt(text, key), key))
        
        elif choice == 3:
            inp_text = input('Enter the encrypted text: ')
            enc_text = inp_text.lower()
            print()
            possible_original_key, possible_original_text = Q3.letter_frequency_attack(enc_text)
            for i in range(10):
                print(f'{i+1}. Possible original key: {possible_original_key[i]}\n'
                    f'Possible original text: {possible_original_text[i]}\n')
        
        elif choice == 4:
            inp_text = input('Enter the encrypted text: ')
            enc_text = inp_text.lower()
            print()
            possible_original_key, possible_original_text = Q4.letter_frequency_attack(enc_text)
            if not possible_original_text:
                print("Please enter long enough data to perform frequency attack.")
                return
            for i in range(10):
                print(f'{i+1}. Possible key: a = {possible_original_key[i][0]}, b = {possible_original_key[i][1]}\n'
                    f'Possible original text: {possible_original_text[i]} \n')
        
        elif choice == 5:
            print("******************HILL CIPHER*******************")
            inp_text = input("Enter text: ")
            inp_key = input("Enter String key: ")
            print("\n")
            HillCipher.result(inp_text, inp_key)
        
        elif choice == 0:
            print("Exit")
            break
        else :
            print("\nPlease enter Valid Input:")


if __name__ == "__main__":
    main()
