# Hill Cipher Decryption Program
# Jean Paul Denata 215314107

import numpy as np

# Matrix for the key
keyMatrix = [[0] * 3 for i in range(3)]

# Create matrix for the message
messageMatrix = [[0] for i in range(3)]

# Create matrix for the cipher
cipherMatrix = [[0] for i in range(3)]

# Matrix for the key (Transpose)
keyMatrixTranspose = [[0] * 3 for i in range(3)]

minorDeterminant = [[0 for j in range(3)] for i in range(3)]

inverseMatrix = [[0] * 3 for i in range(3)]

# Function to generate key matrix from the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def modInverseTest(main):
    n = 1
    while (main * n) % 26 != 1:
        n += 1
    return n

def matrixInverse():
    keyMatrixTranspose = np.transpose(np.array(keyMatrix))
    for i in range(3):
        for j in range(3):
            minorDeterminant[i][j]= determinant(keyMatrixTranspose, i, j)
    inverseMatrixTemp = np.array(minorDeterminant) % 26
    multiplier = modInverseTest(getDeterminant(keyMatrix))
    inverseMatrixTemp = (multiplier * inverseMatrixTemp) % 26
    return inverseMatrixTemp

def determinant(matrix, row, col):
    minor_matrix = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
    determinant = int(np.round(np.linalg.det(minor_matrix)))
    if (row == 0 and col == 1) or (row == 1 and col == 0) or(row == 1 and col == 2) or (row == 2 and col == 1):
        determinant = determinant * (-1)
    return determinant

def getDeterminant(matrix):
    return np.round(np.linalg.det(matrix))

def decrypt(cipher, inverse):

    for i in range(3):
        for j in range(1):
            messageMatrix[i][j] = 0
            for x in range(3):
                messageMatrix[i][j] += (inverse[i][x] * cipher[x][j])
            messageMatrix[i][j] = messageMatrix[i][j] % 26

def HillCipher(cipher, key):

    # Get the key matrix from the key string
    getKeyMatrix(key)

    # Create the inverse key matrix
    inverseMatrix = matrixInverse()

    # Create matrix for the cipher
    for i in range(3):
        cipherMatrix[i][0] = ord(cipher[i]) % 65
    
    # Generate the decrypted matrix
    decrypt(cipherMatrix, inverseMatrix)

    # Generate the decrypted text
    decryptedText = []
    for i in range(3):
        decryptedText.append(chr(messageMatrix[i][0] + 65))
    return decryptedText


# Main function
def main():
    print('----------------------------------')
    print('  Hill Cipher Decryption Program ')
    print('----------------------------------')
    print('- Jean Paul Denata 215314107')
    print()
    print()

    while True:
        cipher = input('Cipher: ')
        parts = cipher.split()
        cipherWithoutSpaces = "".join(parts)
        resultArray = [cipherWithoutSpaces[i:i+3] for i in range(0, len(cipherWithoutSpaces), 3)]

        key = input('Key: ')

        print('Plaintext:', end=' ')
        for i in resultArray:
            result = HillCipher(i, key)
            for h in result:
                print(h, end='')

        print()

        choice = input('Do you want to decrypt again? [y/n]')
        if choice.lower() != 'y':
            break  # Exit the loop if the answer is not 'y'

if __name__ == "__main__":
    main()
