# Import de la fonction de chiffrement, de déchiffrement et de Kasiski de Vigenère
from fonctions.chiffrementDeVigenere import encryptionDeVigenere
from fonctions.dechiffrementDeVigenere import dechiffrageDeVigenere
from fonctions.kasikiExaminationClef import examen_kasiski
from fonctions.config import chemin_clef

def sauvegarder_clef(clef):
    with open(chemin_clef, 'w', encoding='utf-8') as fichier:
        fichier.write(clef)

def lire_derniere_clef():
    try:
        with open(chemin_clef, 'r', encoding='utf-8') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return "Aucune clé n'a été enregistrée."

if __name__ == '__main__':

    while True:
        print("\nBienvenue dans ce programme de chiffrement et de déchiffrement de données\n"
              "Veuillez choisir une option :\n"
              "1. Chiffrer un texte\n"
              "2. Déchiffrer un texte\n"
              "3. Trouver la taille de la clé avec la méthode de Kasiski\n"
              "4. Afficher la dernière clé de chiffrement utilisée\n"
              "5. Quitter\n")

        choix = input("Votre choix (1, 2, 3, 4 ou 5) : ")

        if choix == '1':
            # Récupération du texte à chiffrer et de la clé de chiffrement
            texteEnEntree = input("Veuillez rentrer le texte à chiffrer : ")
            clefDeChiffrementDeVigenere = input("Veuillez rentrer la clé de chiffrement : ")

            # Sauvegarder la clé dans un fichier
            sauvegarder_clef(clefDeChiffrementDeVigenere)

            # Appel de la fonction de chiffrement de Vigenère
            texteEncrypte = encryptionDeVigenere(texteEnEntree, clefDeChiffrementDeVigenere)

            # Affichage du texte chiffré
            print("Le texte chiffré est : ", texteEncrypte)

        elif choix == '2':
            # Récupération du texte à déchiffrer et de la clé de déchiffrement
            texteEncrypte = input("Veuillez rentrer le texte à déchiffrer : ")
            clefDeChiffrementDeVigenere = input("Veuillez rentrer la clé de déchiffrement : ")

            # Sauvegarder la clé dans un fichier
            sauvegarder_clef(clefDeChiffrementDeVigenere)

            # Appel de la fonction de déchiffrement de Vigenère
            texteDecrypte = dechiffrageDeVigenere(texteEncrypte, clefDeChiffrementDeVigenere)

            # Affichage du texte déchiffré
            print("Le texte déchiffré est : ", texteDecrypte)

        elif choix == '3':
            # Récupération du chemin du fichier à analyser
            file_path = input("Veuillez rentrer le chemin du fichier à analyser : ")

            # Appel de la fonction de Kasiski
            taille_potentielle_clef = examen_kasiski(file_path)

            # Affichage de la taille potentielle de la clé
            if taille_potentielle_clef:
                print(f"La taille potentielle de la clé est : {taille_potentielle_clef}")
            else:
                print("Impossible de déterminer la taille de la clé.")

        elif choix == '4':
            # Afficher la dernière clé de chiffrement utilisée
            derniere_clef = lire_derniere_clef()
            print(f"La dernière clé de chiffrement utilisée est : {derniere_clef}")

        elif choix == '5':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, 4 ou 5.")