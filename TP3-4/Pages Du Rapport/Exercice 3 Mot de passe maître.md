# Exercice 3 : Mot de passe maître

Dans cette étape, le code a été modifié pour prendre en compte un mot de passe maître, stocké dans un fichier nommé `mpwd`. Ce mot de passe maître sert de base pour générer des mots de passe en fonction de la taille et du tag fourni. Le programme gère également la création, la vérification et le changement de ce mot de passe maître, en respectant certaines contraintes, comme l'absence d'espaces et la possibilité de le modifier via la console.

```python
contenu de mpwd.txt : vide 

Voulez-vous changer le mot de passe maître ? (oui/non) : non
Voulez-vous changer le mot de passe maître ? (oui/non) : oui
Entrez un nouveau mot de passe maître (sans espaces) : fdhsjkfdjskhsjlkldksaj fdshjfldshjk
Le mot de passe maître ne doit pas contenir d'espaces.
Entrez un nouveau mot de passe maître (sans espaces) : hjksdfhjklsdf89er89-
Entrez la chaîne de caractères : fghbjdshgjfd
Entrez la taille du mot de passe attendu (1-12) : 34
N doit être compris entre 1 et 12. Veuillez réessayer.
Entrez la taille du mot de passe attendu (1-12) : 231
N doit être compris entre 1 et 12. Veuillez réessayer.
Entrez la taille du mot de passe attendu (1-12) : 12
Mot de passe généré : MQeygKuKL4ZY
```

```python
contenu de mpwd.txt : hjksdfhjklsdf89er89-

Voulez-vous changer le mot de passe maître ? (oui/non) : non
Entrez la chaîne de caractères : hdjfksayhuerdfjs-'/
Entrez la taille du mot de passe attendu (1-12) : 5
Mot de passe généré : ykFs/
```