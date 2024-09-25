#Ce fichier est le fichier principal du projet. Il contient le code qui permet de lancer le programme.
#Il importe les fonctions de chiffrement et de déchiffrement de Vigenère, et les utilise pour chiffrer et déchiffrer un texte.
#Il affiche également un message de bienvenue et des instructions pour l'utilisateur.
#Programme réalisé en français avec une convention de nommage en français en camelCase.

#Import de la fonction de chiffrement de Vigenère
from fonctions.chiffrementDeVigenere import encryptionDeVigenere


if __name__ == '__main__':

    print("Bienvenue dans ce programme de chiffrement de données\n"
          "Veuillez rentrer un texte à chiffrer et une clé de chiffrement pour continuer.\n")

    #Récupération du texte à chiffrer et de la clé de chiffrement
    texteEnEntree = input("Veuillez rentrer le texte à chiffrer : ")
    clefDeChiffrementDeVigenere = input("Veuillez rentrer la clé de chiffrement : ")

    #appel de la fonction de chiffrement de Vigenère presente dans /fonctions/chiffrementDeVigenere.py
    texteEncrypte = encryptionDeVigenere(texteEnEntree, clefDeChiffrementDeVigenere)

    #Affichage du texte chiffré
    print("Le texte chiffré est : ", texteEncrypte)







