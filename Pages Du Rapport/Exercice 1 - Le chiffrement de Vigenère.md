# Exercice 1 - Le chiffrement de Vigenère

Le TP est composé de plusieurs parties, la première étant le chiffrement de Vigenère. Nous devons réaliser l'implémentation du chiffrement tout en portant attention aux détails en faisant des choix d'implémentation comme les lettres majuscules et minuscules, mais aussi la ponctuation et les caractères spéciaux, sans oublier les espaces.

## Les choix effectués pour le chiffrement du texte

[chiffrementDeVigenere.py](http://chiffrementdevigenere.py/) [chiffrementDeVigenere.py](http://chiffrementdevigenere.py/) effectue le chiffrement de Vigenère sur le texte d'entrée en utilisant la clé fournie. Voici une explication étape par étape de ce que fait la fonction et comment elle gère différents types de caractères :

Validation de l'entrée :

La fonction vérifie d'abord si le texte d'entrée ou la clé est vide ou ne contient que des espaces. Si l'un ou l'autre est invalide, elle lève une ValueError.

## Préparation de la clé :

La fonction supprime tous les espaces de la clé pour s'assurer qu'elle est continue.

## Répétition de la clé :

```python
 clef_Repetee = (clefDeChiffrementDeVigenere * (len(texteEnEntree) // len(clefDeChiffrementDeVigenere))) + clefDeChiffrementDeVigenere[:len(texteEnEntree) % len(clefDeChiffrementDeVigenere)]

```

La clé est répétée pour correspondre à la longueur du texte d'entrée. Cela se fait en répétant la clé suffisamment de fois, puis en prenant la sous-chaîne nécessaire pour correspondre exactement à la longueur du texte d'entrée.

## Processus de chiffrement :

La fonction itère sur chaque caractère du texte d'entrée.

Si le caractère est un espace, il est directement ajouté au texte chiffré sans aucun changement.
Pour les autres caractères, la fonction calcule le caractère chiffré en ajoutant les valeurs ASCII du caractère d'entrée et du caractère correspondant de la clé, puis en prenant le résultat modulo 128 pour s'assurer qu'il reste dans la plage ASCII. Le caractère résultant est ensuite ajouté au texte chiffré.

## Gestion des différents caractères :

Espaces : Les espaces dans le texte d'entrée sont conservés comme des espaces dans le texte chiffré.

Lettres majuscules et minuscules : Les deux sont traitées de la même manière, car la fonction opère directement sur les valeurs ASCII.

Caractères spéciaux : Tous les caractères spéciaux sont également chiffrés en utilisant leurs valeurs ASCII, ce qui garantit qu'ils restent dans la plage ASCII après chiffrement.

```python
    for i in range(len(texteEnEntree)):
        if texteEnEntree[i] == ' ':
            texteEncrypte += ' '
        else:
            char_index = ord(texteEnEntree[i])
            key_index = ord(clef_Repetee[i])
            encrypted_index = (char_index + key_index) % 128  # On utilise 128 pour couvrir tous les caractères ASCII
            texteEncrypte += chr(encrypted_index)
```

Cette implémentation du chiffrement de Vigenère offre une solution robuste et flexible pour le chiffrement de textes. Elle prend en compte divers aspects importants :

- Gestion des espaces : préserve la structure visuelle du texte original
- Traitement uniforme des majuscules et minuscules : simplifie le processus tout en maintenant la diversité des caractères
- Prise en charge des caractères spéciaux : assure que tout type de texte peut être chiffré
- Utilisation de l'ensemble de la table ASCII : augmente la complexité et la sécurité du chiffrement

Cette approche permet de chiffrer efficacement une grande variété de textes tout en conservant leur structure générale, ce qui est particulièrement utile pour des applications pratiques du chiffrement de Vigenère.