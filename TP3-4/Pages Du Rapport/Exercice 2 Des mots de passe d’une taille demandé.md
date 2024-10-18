# Exercice 2 : Des mots de passe d’une taille demandée

Dans cette sous-partie, nous allons explorer une extension de notre programme initial. L'objectif est de créer un système plus flexible qui permet à l'utilisateur de spécifier la longueur souhaitée pour le mot de passe généré. Voici les principales caractéristiques de cette nouvelle version :

- Entrées : un entier N (1 ≤ N ≤ 12) et deux chaînes de caractères
    - N détermine la taille du mot de passe généré
    - Les deux chaînes sont utilisées comme dans l'exercice précédent
- Modifications potentielles :
    - Adaptation de la fonction de hachage pour des sorties plus longues si nécessaire

Pour valider cette nouvelle fonctionnalité, nous procéderons à une série de tests rigoureux. Dans les sections suivantes, nous présenterons les jeux d'essais les plus pertinents ainsi qu'une liste complète de cas de tests pour assurer la robustesse de notre programme.

```python
Input: (/njkj[p[kjjkofdasmbjskldfhejwqkldvbfuiowdvgfswpoifhdjewkdsngiy3uejdscnbfjriueodjsck, fdsDW2345+-*-/-*//*-//*-*/4-45*4*fdhaejgydhusjdkabsgetuidjskcbshreuwidjsksreyuiwdsjvbrhkyui-, 8) => Output: flqH2eQA
Input: (Hello, World, 5) => Output: iuauc
Input: (123, 456, 12) => Output: ujJTh2rta8It
Input: (abc, def, 1) => Output: 4
Input: (, , 10) => Output: z4PhNX7vuL
Input: (special*&^%$, characters!@#, 6) => Output: d59GDD
Input: (Hello, World, 14) => Error: N doit être compris entre 1 et 12
Input: (Hello, World, 0) => Error: N doit être compris entre 1 et 12
```