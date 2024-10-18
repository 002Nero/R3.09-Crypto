# Exercice 4 : Attaques sur des mots de passe

Dans cette section, nous tentons de compromettre la sécurité du générateur de mots de passe en recherchant des préimages du mot de passe maître. L'objectif est de trouver un mot de passe maître valide en utilisant uniquement le tag, sans connaître le mot de passe maître. L'attaque est menée par dictionnaire, en testant toutes les combinaisons possibles pour un mot de passe maître de 10 caractères, afin de provoquer une collision. Cette analyse nous permet d'estimer la difficulté de casser le générateur en fonction de la taille des mots de passe et du nombre de tags utilisés.

Combien de possibilités essayées ?
Le code compte le nombre de tentatives effectuées pour trouver un mot de passe maître qui provoque une collision pour le tag "Unilim". Le nombre total de combinaisons possibles pour un mot de passe de 10 caractères, avec 62 caractères possibles (26 lettres minuscules + 26 lettres majuscules + 10 chiffres), est (62^{10}).

Probabilité théorique de trouver un mot de passe maître qui provoque une collision
La probabilité théorique de trouver un mot de passe maître qui provoque une collision dépend de la taille de l'espace de recherche et de la longueur du hash tronqué. Pour un hash de longueur (N), il y a (64^N) possibilités (puisque le hash est encodé en base64). La probabilité de collision est donc (1 / 64^N).

Comparaison du nombre d'essais avec la probabilité théorique
Votre code retourne le nombre de tentatives effectuées pour trouver une collision. Vous pouvez comparer ce nombre avec la probabilité théorique en calculant le ratio entre le nombre d'essais et (64^N).

Exemple de calcul
Pour (N = 8):

Nombre total de combinaisons possibles : (62^{10})
Probabilité théorique de collision : (1 / 64^8)

```python
Collision sur les 3 tags 'Amazon' 'Unilim' 'Netflix'

Mots de passe générés pour les tags avec N=1 : {'Unilim': 'U', 'Amazon': 'W', 'Netflix': 'p'}
Mot de passe maître trouvé pour N=1 : aaaaaaaa3Z en 3462 tentatives
Mots de passe générés pour les tags avec N=2 : {'Unilim': 'Ux', 'Amazon': 'Wo', 'Netflix': 'pO'}
Mot de passe maître trouvé pour N=2 : aaaaaap5dh en 3794222 tentatives

N = 3 : impossible trop de combinaisons sont possible et le programme devrais tourner
pendant beaucoup trop longtemps.
```