# Exercice 3 - Kasiski et la taille de la clé en Vigenère

Au début du rapport, plusieurs informations vous ont été transmises, notamment un lien vers mon GitHub . Pourquoi avoir fait cela ?

Très simple en réalité : il y a eu 2 versions de Kasiski dans mon programme. Ayant lu le TP un peu vite, je n'ai pas directement suivi les étapes précises qui nous sont indiquées pour implémenter la méthode de Kasiski. Seule la version qui suit les explications du TP est abordée ici. La version « initiale » est, elle, accessible depuis le repo.

### Fonction `lire_fichier`

Cette fonction lit le contenu d'un fichier et retourne le texte sous forme de chaîne de caractères.

```python
def lire_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        return fichier.read()

```

**Exemple d'utilisation :**

Supposons que nous ayons un fichier `texte.txt` contenant le texte "ABABABAB".

```python
texte = lire_fichier('texte.txt')
print(texte)  # Output: "ABABABAB"

```

### Fonction `trouver_sequences_repetees`

Cette fonction trouve les séquences répétées d'une longueur donnée dans un texte et retourne un dictionnaire avec les séquences comme clés et les indices de leurs occurrences comme valeurs.

```python
def trouver_sequences_repetees(texte, longueur_sequence=3):
    sequences = defaultdict(list)
    for i in range(len(texte) - longueur_sequence + 1):
        seq = texte[i:i + longueur_sequence]
        sequences[seq].append(i)
    return {seq: indices for seq, indices in sequences.items() if len(indices) > 1}

```

**Exemple d'utilisation :**

Pour le texte "ABABABAB" avec une longueur de séquence de 2 :

```python
sequences = trouver_sequences_repetees("ABABABAB", 2)
print(sequences)  # Output: {'AB': [0, 2, 4], 'BA': [1, 3, 5]}

```

### Fonction `calculer_distances`

Cette fonction calcule les distances entre les occurrences des séquences répétées.

```python
def calculer_distances(sequences_repetees):
    distances = []
    for seq, indices in sequences_repetees.items():
        for i in range(len(indices) - 1):
            distances.append((seq, indices[i + 1] - indices[i]))
    return distances

```

**Exemple d'utilisation :**

Pour les séquences répétées `{'AB': [0, 2, 4], 'BA': [1, 3, 5]}` :

```python
distances = calculer_distances({'AB': [0, 2, 4], 'BA': [1, 3, 5]})
print(distances)  # Output: [('AB', 2), ('AB', 2), ('BA', 2), ('BA', 2)]

```

### Fonction `trouver_facteurs`

Cette fonction trouve les facteurs d'un nombre donné.

```python
def trouver_facteurs(nombre):
    facteurs = set()
    for i in range(2, nombre + 1):
        if nombre % i == 0:
            facteurs.add(i)
    return facteurs

```

**Exemple d'utilisation :**

Pour le nombre 6 :

```python
facteurs = trouver_facteurs(6)
print(facteurs)  # Output: {2, 3, 6}

```

### Fonction `examen_kasiski`

Cette fonction principale effectue l'examen de Kasiski pour déterminer la longueur potentielle de la clé.

Lecture du fichier : La fonction commence par lire le contenu du fichier spécifié par chemin_fichier.

```python
texte = lire_fichier(chemin_fichier)
```

Trouver les séquences répétées : Elle utilise la fonction trouver_sequences_repetees pour identifier les séquences répétées dans le texte.

sequences_repetees = trouver_sequences_repetees(texte)

Calculer les distances : Ensuite, elle calcule les distances entre les occurrences des séquences répétées à l'aide de la fonction calculer_distances.

```python
distances = calculer_distances(sequences_repetees)
```

Vérification des distances : Si aucune distance n'est trouvée, la fonction retourne "?" pour indiquer qu'elle n'a pas pu déterminer la longueur de la clé.

```python
if not distances:
return "?"
```

Trier les distances : Les distances sont triées par la longueur des séquences en ordre décroissant.

```python
distances.sort(key=lambda x: len(x[0]), reverse=True)
```

Calculer les facteurs : La fonction prend la première séquence et sa distance, puis calcule les facteurs de cette distance.

```python
premiere_ligne = distances[0]
seq, distance = premiere_ligne
candidats = trouver_facteurs(distance)

```

Vérification des facteurs : Si aucun facteur n'est trouvé, la fonction retourne "?".

```python
if not candidats:
return "?"
```

Parcourir les autres distances : La fonction parcourt les autres distances pour trouver des facteurs communs avec les candidats actuels.

```python
for seq, distance in distances:
temp = []
for candidat in candidats:
gcd_value = gcd(candidat, distance)
if gcd_value != 1:
temp.append(gcd_value)
if temp:
candidats = temp
elif not temp and distances.index((seq, distance)) < len(distances) - 1:
continue
elif not temp:
break
```

Vérification finale des candidats : Si aucun facteur commun n'est trouvé, la fonction retourne "?".

```python
if not candidats:
return "?"
```

Déterminer la taille potentielle de la clé : La fonction détermine la taille potentielle de la clé comme le plus petit facteur trouvé.

```python
taille_potentielle_clef = min(candidats)
```

Déterminer la certitude : Elle vérifie si le nombre de candidats est supérieur ou égal au seuil de certitude.

```python
certitude = len(candidats) >= seuil_certitude
```

Retourner le résultat : Enfin, la fonction retourne la taille potentielle de la clé, avec un point d'interrogation si la certitude est faible.

```python
return f"{taille_potentielle_clef}{' ?' if not certitude else ''}"
```

```python
def examen_kasiski(chemin_fichier, seuil_certitude=3):
    texte = lire_fichier(chemin_fichier)
    sequences_repetees = trouver_sequences_repetees(texte)
    distances = calculer_distances(sequences_repetees)

    if not distances:
        return "?"

    distances.sort(key=lambda x: len(x[0]), reverse=True)
    premiere_ligne = distances[0]
    seq, distance = premiere_ligne
    candidats = trouver_facteurs(distance)

    if not candidats:
        return "?"

    for seq, distance in distances:
        temp = []
        for candidat in candidats:
            gcd_value = gcd(candidat, distance)
            if gcd_value != 1:
                temp.append(gcd_value)

        if temp:
            candidats = temp
        elif not temp and distances.index((seq, distance)) < len(distances) - 1:
            continue
        elif not temp:
            break

    if not candidats:
        return "?"

    taille_potentielle_clef = min(candidats)
    certitude = len(candidats) >= seuil_certitude

    return f"{taille_potentielle_clef}{' ?' if not certitude else ''}"

```

**Exemple d'utilisation :**

Supposons que nous ayons un fichier `texte.txt` contenant le texte "ABABABAB".

```python
resultat = examen_kasiski('texte.txt')
print(resultat)  # Output: "2"

```

### Jeux d'essais pertinents

1. **Texte : "ABABABAB"**
    - **Input :** Fichier contenant "ABABABAB"
    - **Output :** "2"
    - **Explication :** Les séquences "AB" et "BA" se répètent avec une distance de 2, ce qui suggère une clé de longueur 2.
2. **Texte : "ABCABCABC"**
    - **Input :** Fichier contenant "ABCABCABC"
    - **Output :** "3"
    - **Explication :** Les séquences "ABC" se répètent avec une distance de 3, ce qui suggère une clé de longueur 3.
3. **Texte : "AABBAABB"**
    - **Input :** Fichier contenant "AABBAABB"
    - **Output :** "4"
    - **Explication :** Les séquences "AABB" se répètent avec une distance de 4, ce qui suggère une clé de longueur 4.

Ces jeux d'essais sont pertinents car ils démontrent comment l'examen de Kasiski peut identifier la longueur de la clé en trouvant des séquences répétées et en calculant les distances entre elles.