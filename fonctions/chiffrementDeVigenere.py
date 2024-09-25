#Fonction de chiffrement de Vigenère
#Cette fonction prend en paramètre un texte en clair et une clé de chiffrement, et retourne le texte chiffré.
#Entrée : texte en clair, clé de chiffrement
#Sortie : texte chiffré


def encryptionDeVigenere(texteEnEntree, clefDeChiffrementDeVigenere):
   texteEncrypte = ''
   # Repete en boucle la clef de chiffrement jusqu'a atteindre la longueur du texte en entree
   clef_Repetee = (clefDeChiffrementDeVigenere * (len(texteEnEntree) // len(clefDeChiffrementDeVigenere))) + clefDeChiffrementDeVigenere[:len(texteEnEntree) % len(clefDeChiffrementDeVigenere)]
   # Iteration pour chaque caractere
   for i in range(len(texteEnEntree)):
       # On regarde si le texte est bien une lettre de l'alphabet
       if texteEnEntree[i].isalpha():
           # Calcul du changement a effectue base sur la clef et le texte en entree
           changementDeCaractere = ord(clef_Repetee[i].upper()) - ord('A')
           # Chaque caractere alphabetique est encrypter differement s'il est en majuscule ou non
           if texteEnEntree[i].isupper():
               texteEncrypte += chr((ord(texteEnEntree[i]) + changementDeCaractere - ord('A')) % 26 + ord('A'))
           else:
               texteEncrypte += chr((ord(texteEnEntree[i]) + changementDeCaractere - ord('a')) % 26 + ord('a'))
       else:
           # Pour le moment seuls les caracteres alphabetiques sont pris en compte
           # Les autres caracteres comme la ponctuation reste inchangee dans cette version du programme
           texteEncrypte += texteEnEntree[i]
   # Retour du texte maintenant encrypte
   return texteEncrypte