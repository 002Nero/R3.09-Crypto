# Function to encrypt text using Vigenere cipher
# This function takes a plaintext and an encryption key as parameters, and returns the encrypted text.
# Input: plaintext, encryption key
# Output: encrypted text

def encryptionDeVigenere(texteEnEntree, clefDeChiffrementDeVigenere):
    if not clefDeChiffrementDeVigenere.strip():
        raise ValueError("The encryption key cannot be empty or only spaces")

    # On retire les espaces de la clef
    clefDeChiffrementDeVigenere = clefDeChiffrementDeVigenere.replace(' ', '')

    texteEncrypte = ''
    clef_Repetee = (clefDeChiffrementDeVigenere * (len(texteEnEntree) // len(clefDeChiffrementDeVigenere))) + clefDeChiffrementDeVigenere[:len(texteEnEntree) % len(clefDeChiffrementDeVigenere)]

    for i in range(len(texteEnEntree)):
        if texteEnEntree[i] == ' ':
            texteEncrypte += ' '
        else:
            char_index = ord(texteEnEntree[i])
            key_index = ord(clef_Repetee[i])
            encrypted_index = (char_index + key_index) % 128  # Use 128 to cover all ASCII characters
            texteEncrypte += chr(encrypted_index)

    return texteEncrypte