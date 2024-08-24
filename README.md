
![](https://img.shields.io/badge/Python-red?style=for-the-badge&logo=python) 

# Introduction

![image](https://github.com/user-attachments/assets/f3a85d50-9503-4056-a3c1-c22138909db3)


Hill Cipher is one of the classic cryptographic algorithms that utilizes the principles of linear algebra to encrypt and decrypt messages. It works by converting the original text (plaintext) into a numeric vector, then using a key matrix to multiply the vector. The result of this multiplication is a new vector which is then converted back into encrypted text (ciphertext). For the decryption process, the key matrix is inverted (inverse) and used to return the ciphertext to plaintext.
# Pros
- Math-Based Security: Hill Cipher offers strong security as it uses matrices and modular operations that make it difficult to crack with simple brute force methods.
- Simple and Efficient: The algorithm is relatively easy to understand and implement, making it suitable for basic learning purposes about cryptography.
- Resistance to Frequency Analysis: Since the Hill Cipher encrypts blocks of text at a time, this makes it more difficult to analyze using letter frequencies compared to a simple substitution cipher.

# Cons
- Keys Must Be Invertible: The key matrix used must have an inverse modulo 26, which means not all given keys will be valid for encryption and decryption.
- Vulnerable to Known-Plaintext Attacks: If an attacker has access to a pair of plaintext and corresponding ciphertext, they can attempt to reverse the key matrix.
- Limited to a Certain Block Length: Standard Hill Cipher implementations usually work on small blocks (such as 3x3), which can limit the length of messages that can be encrypted at once.



# How it works
## Encryption:
- The user enters the message and key.
- The message is broken into blocks of 3 characters.
- Each block is converted into a numeric vector, then multiplied by the key matrix.
- The result of the multiplication is converted back into encrypted text (ciphertext).

## Decryption:

- The user inputs the ciphertext and the key.
- The key matrix is inverted (inverse) for use in decryption.
- The ciphertext is broken into blocks, converted into a numeric vector, then multiplied by the inverse matrix.
- The result of the multiplication is converted back into the original text (plaintext).
