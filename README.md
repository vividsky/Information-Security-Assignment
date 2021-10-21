# Information-Security-Assignment

Repository for Internet Security Assignment for course MCAC303.

## Contributors:
1. Nidhi Sangwan (29)
2. Rishabh Poria (42)

## Language Used:
* Python 3.9 
  
## Working:

* Different questions of the assignment are placed under separate modules and all of them are accessed from [main.py](https://github.com/vividsky/Information-Security-Assignment/blob/main/main.py)

## 1. CAESAR CIPHER:

Program module: [caesar_cipher.py](https://github.com/vividsky/Information-Security-Assignment/blob/main/caesar_cipher.py)

* [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is a type of [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher) in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

### Output:

|<h3>Encoding</h3>|<h3>Decoding</h3> |
|:---------------:|:----------------:|
| <img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/CaesarCipherEnc.png" width="450"/> |  <img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/CaesarCipherDec.png" width="450"/> |

## 2. AFFINE CIPHER:

Program module: [affine_cipher.py](https://github.com/vividsky/Information-Security-Assignment/blob/main/affine_cipher.py)

* [Affine cipher](https://en.wikipedia.org/wiki/Affine_cipher) is a type of [monoalphabetic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher), where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. 

* Formula used to perform encryption: y = (ax+b) % 26

### Output: 

|<h3>Encoding</h3>|<h3>Decoding</h3> |
|:---------------:|:----------------:|
| <img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/AffineCipherEnc.png" width="450"/> |  <img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/AffineCipherDec.png" width="450"/> |

* One thing to remember while using affine cipher is that value of 'a' should be co-prime with 26 (else several letters might get mapped to the one letter), making the cipher non-monoalphabetic and hence the decryption of encoded text using such a key wont be possible.

## 3. LETTER FREQUENCY ATTACK ON CAESAR CIPHER:

Program module: [freq_attack_caesar.py](https://github.com/vividsky/Information-Security-Assignment/blob/main/freq_attack_caesar.py)

* [Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) is based on the fact that, in any given stretch of written language, certain letters and combinations of letters occur with varying frequencies. Moreover, there is a characteristic distribution of letters that is roughly the same for almost all samples of that language. 

* Letter frequency attacks take advantage of this fact and guess which letter in the ciphertext might belong to which letter in the plaintext.

### Output: 

<img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/LFA_Caesar.png" width="900"/>

* Original plaintext will be present in the output if the most common letter in the plaintext (before encoding) exists in the list ['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u']

## 4. LETTER FREQUENCY ATTACK ON AFFINE CIPHER:

Program module: [freq_attack_affine.py](https://github.com/vividsky/Information-Security-Assignment/blob/main/freq_attack_affine.py)

* Affine cipher being a substitution cipher, is also prone to brute force attacks and letter frequency attacks.

### Output: 

<img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/LFA_Affine.png" width="900"/>

* Affine cipher is a monoalphabetic cipher (i.e. one to one mapping)
* Letter frequency attacks are a little difficult on affine cipher as compared to caesar cipher.
* There is no guarantee that the attack will be successful because:
  - Most used letter pairs might not be present in the list (There are 26 X 25 possibilities)
  - Even after that, modular multiplicative inverse of 'a' might not exist
  - We might have picked smaller value of 'a' than the actual value of 'a'
 
## 5. 2X2 HILL CIPHER:

Program module: [hill_cipher.py](https://github.com/vividsky/Information-Security-Assignment/blob/main/hill_cipher.py)

* [Hill cipher](https://en.wikipedia.org/wiki/Hill_cipher) is a [polygraphic substitution cipher](https://en.wikipedia.org/wiki/Polygraphic_substitution) based on linear algebra. Invented by Lester S. Hill in 1929, it was the first polygraphic cipher in which it was practical (though barely) to operate on more than three symbols at once.

* Here we use 2X2 version of this cipher.

### Output: 

|<h3>Encoding</h3>|<h3>Decoding</h3> |
|:---------------:|:----------------:|
| <img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/HillCipherEnc.png" width="450"/> |  <img src="https://github.com/vividsky/Information-Security-Assignment/blob/main/Ouput_Images/HillCipherDec.png" width="450"/> |

* Similar to affine cipher, decryption of hill cipher encoded text will not be possible if the 2X2 key matrix is not invertible.
