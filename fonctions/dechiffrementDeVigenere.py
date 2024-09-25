# Fonction pour dechiffrer le texte chiffré avec Vigenère
# Cette fonction prends en paramètre le texte chiffré et la clé de déchiffrement et retourne le texte déchiffré.
# Entree : texte chiffré, clé de déchiffrement
# Sortie : texte déchiffré

def dechiffrageDeVigenere(texteEncrypte, clefDeChiffrementDeVigenere):
    if not texteEncrypte.strip():
        raise ValueError("Le texte chiffré ne peut être vide ou constitué uniquement d'espaces")
    if not clefDeChiffrementDeVigenere.strip():
        raise ValueError("La clé ne peut être vide ou constituée uniquement d'espaces")

    # Supprimer les espaces du texte chiffré et de la clé de chiffrement
    clefDeChiffrementDeVigenere = clefDeChiffrementDeVigenere.replace(' ', '')

    texteDecrypte = ''
    clef_Repetee = (clefDeChiffrementDeVigenere * (len(texteEncrypte) // len(clefDeChiffrementDeVigenere))) + clefDeChiffrementDeVigenere[:len(texteEncrypte) % len(clefDeChiffrementDeVigenere)]

    for i in range(len(texteEncrypte)):
        if texteEncrypte[i] == ' ':
            texteDecrypte += ' '
        else:
            char_index = ord(texteEncrypte[i])
            key_index = ord(clef_Repetee[i])
            dechiffrage_index = (char_index - key_index) % 128  # Use 128 to cover all ASCII characters
            texteDecrypte += chr(dechiffrage_index)

    return texteDecrypte