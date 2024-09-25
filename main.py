# Import de la fonction de chiffrement et de déchiffrement de Vigenère
from fonctions.chiffrementDeVigenere import encryptionDeVigenere
from fonctions.dechiffrementDeVigenere import dechiffrageDeVigenere

if __name__ == '__main__':

    print("Bienvenue dans ce programme de chiffrement et de déchiffrement de données\n"
          "Veuillez choisir une option :\n"
          "1. Chiffrer un texte\n"
          "2. Déchiffrer un texte\n")

    choix = input("Votre choix (1 ou 2) : ")

    if choix == '1':
        # Récupération du texte à chiffrer et de la clé de chiffrement
        texteEnEntree = input("Veuillez rentrer le texte à chiffrer : ")
        clefDeChiffrementDeVigenere = input("Veuillez rentrer la clé de chiffrement : ")

        # Appel de la fonction de chiffrement de Vigenère
        texteEncrypte = encryptionDeVigenere(texteEnEntree, clefDeChiffrementDeVigenere)

        # Affichage du texte chiffré
        print("Le texte chiffré est : ", texteEncrypte)

    elif choix == '2':
        # Récupération du texte à déchiffrer et de la clé de déchiffrement
        texteEncrypte = input("Veuillez rentrer le texte à déchiffrer : ")
        clefDeChiffrementDeVigenere = input("Veuillez rentrer la clé de déchiffrement : ")

        # Appel de la fonction de déchiffrement de Vigenère
        texteDecrypte = dechiffrageDeVigenere(texteEncrypte, clefDeChiffrementDeVigenere)
# TJ Xh^\ eOX QMD]ThheZ je ne suis pas une chaussure
        # Affichage du texte déchiffré
        print("Le texte déchiffré est : ", texteDecrypte)

    else:
        print("Choix invalide. Veuillez relancer le programme et choisir 1 ou 2.")