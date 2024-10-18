# Exercice 1 : Des mots de passe tout simples

Partie 1 : Génération de mots de passe simples

Dans cette première étape, nous avons développé une application qui génère un mot de passe de 8 caractères à partir de deux chaînes de caractères arbitraires. L'algorithme suit ces étapes :

1. **Concaténation des deux chaînes d'entrée** : Les deux chaînes sont combinées pour créer une seule chaîne.
2. **Hachage de la chaîne** : Cette chaîne concaténée est ensuite hachée à l'aide d'une fonction cryptographique (comme SHA256).Ici, nous utiliserons SHA-512 et non SHA-256, car SHA-256 posait certains problèmes, notamment pour la création de mots de passe longs. Il n'arrivait pas à générer, à partir du hachage, un mot de passe de 8 caractères. De plus, SHA-512 permet de retirer les caractères « invisibles » ou non affichables. 
3. **Extraction du mot de passe** : Les caractères obtenus du hachage sont transformés pour produire une chaîne de 8 caractères composée de lettres (majuscules et minuscules), chiffres et symboles spéciaux.

```python
str1 = "/njkj[p[kjjkofdasmbjskldfhejwqkldvbfuiowdvgfswpoifhdjewkdsngiy3uejdscnbfjriueodjsck"
str2 = "fdsDW2345+-*-/-*//*-//*-*/4-45*4*fdhaejgydhusjdkabsgetuidjskcbshreuwidjsksreyuiwdsjvbrhkyui-"
output = flqH2eQA

str1 = "/"
str2 = "f"
output = 5sISMBbj
```