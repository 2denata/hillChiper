# Hill Cipher Encryption Program
# Jean Paul Denata 215314107

# Matrix for the key
keyMatrix = [[0] * 3 for i in range(3)]

# Create matrix for the message
messageMatrix = [[0] for i in range(3)]

# Create matrix for the cipher
cipherMatrix = [[0] for i in range(3)]

# Function to generate key matrix from the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to encrypt the message
def encrypt(messageMatrix):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageMatrix[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):

    # Get the key matrix from the key string
    getKeyMatrix(key)

    # Create matrix for the message
    for i in range(3):
        messageMatrix[i][0] = ord(message[i]) % 65

    # Generate the encrypted matrix
    encrypt(messageMatrix)

    # Generate the encrypted text
    encryptedText = []
    for i in range(3):
        encryptedText.append(chr(cipherMatrix[i][0] + 65))
    return encryptedText
    

# Main function
def main():
    print('----------------------------------')
    print('  Hill Cipher Encryption Program ')
    print('----------------------------------')
    print('- Jean Paul Denata 215314107')
    print()
    print()

    while True:
        # Get the message to be encrypted
        message = input('Message: ')
        
        # Modify the message to remove spaces
        parts = message.split()
        textWithoutSpaces = "".join(parts)
        
        resultArray = [textWithoutSpaces[i:i+3] for i in range(0, len(textWithoutSpaces), 3)]
        
        # Get the key
        key = input('Key: ')
        # key = "RRFVSVCCT"
        
        print('Ciphertext:', end=' ')
        for i in resultArray:
            result = HillCipher(i, key)
            for h in result:
                print(h, end='')
        print()
        

        choice = input('Do you want to encrypt again? [y/n]')
        if choice.lower() != 'y':
            break  # Exit the loop if the answer is not 'y'

if __name__ == "__main__":
    main()
