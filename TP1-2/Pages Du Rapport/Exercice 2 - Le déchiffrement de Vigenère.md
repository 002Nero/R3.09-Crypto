# Exercice 2 - Le déchiffrement de Vigenère

La seconde partie du TP fait écho à la première. Maintenant que nous avons réussi à chiffrer un texte d'entrée avec une clé que l'utilisateur choisit, il est temps de lui implémenter de quoi déchiffrer un texte, si bien sûr il possède la clé. Dans cette partie, on explique avec les parties du code correspondantes comment nous déchiffrons avec la clé un texte chiffré sous Vigenère.

[dechiffrementDeVigenere.py](http://dechiffrementdevigenere.py/) effectue le déchiffrement du chiffre de Vigenère sur le texte chiffré en utilisant la clé fournie. 

## Définition de la fonction et validation de l'entrée

```python
def dechiffrageDeVigenere(texteEncrypte, clefDeChiffrementDeVigenere):
    if not texteEncrypte.strip():
        raise ValueError("Le texte chiffré ne peut être vide ou constitué uniquement d'espaces")
    if not clefDeChiffrementDeVigenere.strip():
        raise ValueError("La clé ne peut être vide ou constituée uniquement d'espaces")
```

Définition de la fonction : La fonction dechiffrageDeVigenere prend deux paramètres : texteEncrypte (le texte chiffré) et clefDeChiffrementDeVigenere (la clé de déchiffrement).

Validation de l'entrée : La fonction vérifie si le texte chiffré ou la clé est vide ou ne contient que des espaces. Si l'un ou l'autre est invalide, elle lève une ValueError.

## Répétition de la clé

```python
texteDecrypte = ''
    clef_Repetee = (clefDeChiffrementDeVigenere * (len(texteEncrypte) // len(clefDeChiffrementDeVigenere))) + clefDeChiffrementDeVigenere[:len(texteEncrypte) % len(clefDeChiffrementDeVigenere)]
```

Initialisation du texte déchiffré : Une chaîne vide texteDecrypte est initialisée pour stocker le texte déchiffré.
Répétition de la clé : La clé est répétée pour correspondre à la longueur du texte chiffré. Cela se fait en répétant la clé suffisamment de fois, puis en prenant la sous-chaîne nécessaire pour correspondre exactement à la longueur du texte chiffré.

## Processus de déchiffrement

```python
for i in range(len(texteEncrypte)):
        if texteEncrypte[i] == ' ':
            texteDecrypte += ' '
        else:
            char_index = ord(texteEncrypte[i])
            key_index = ord(clef_Repetee[i])
            dechiffrage_index = (char_index - key_index) % 128  # Use 128 to cover all ASCII characters
            texteDecrypte += chr(dechiffrage_index)
```

Itération sur le texte chiffré : La fonction itère sur chaque caractère du texte chiffré.
Gestion des espaces : Si le caractère est un espace, il est directement ajouté au texte déchiffré sans aucun changement.

Déchiffrement des autres caractères : Pour les autres caractères, la fonction calcule le caractère déchiffré en soustrayant la valeur ASCII du caractère de la clé de la valeur ASCII du caractère chiffré, puis en prenant le résultat modulo 128 pour s'assurer qu'il reste dans la plage ASCII. Le caractère résultant est ensuite ajouté au texte déchiffré.

Cette implémentation du déchiffrement de Vigenère permet de retrouver le texte original à partir d'un texte chiffré, à condition de connaître la clé utilisée pour le chiffrement. Le processus inverse du chiffrement est appliqué, en soustrayant les valeurs ASCII des caractères de la clé au lieu de les ajouter.

Points clés à retenir :

- La fonction vérifie la validité des entrées pour éviter les erreurs.
- La clé est répétée pour correspondre à la longueur du texte chiffré.
- Le déchiffrement se fait caractère par caractère, en préservant les espaces.
- L'utilisation du modulo 128 assure que le résultat reste dans la plage des caractères ASCII.

Cette implémentation complète le processus de chiffrement vu précédemment, offrant ainsi une solution complète pour le chiffrement et le déchiffrement de Vigenère.

En réalité, cette partie a exactement le même fonctionnement que le chiffrement. La seule différence étant qu'ici nous faisons la manipulation inverse !