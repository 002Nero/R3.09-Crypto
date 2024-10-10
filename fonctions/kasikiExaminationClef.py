import re
from collections import defaultdict
from math import gcd
from functools import reduce


# Fonction pour lire un fichier
def lire_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        return fichier.read()


# Fonction pour trouver les séquences répétées dans un texte
def trouver_sequences_repetees(texte, longueur_sequence=3):
    sequences = defaultdict(list)
    for i in range(len(texte) - longueur_sequence + 1):
        seq = texte[i:i + longueur_sequence]
        sequences[seq].append(i)
    return {seq: indices for seq, indices in sequences.items() if len(indices) > 1}


# Fonction pour calculer les distances entre les séquences répétées
def calculer_distances(sequences_repetees):
    distances = []
    for seq, indices in sequences_repetees.items():
        for i in range(len(indices) - 1):
            distances.append((seq, indices[i + 1] - indices[i]))
    return distances


# Fonction pour trouver les facteurs d'un nombre
def trouver_facteurs(nombre):
    facteurs = set()
    for i in range(2, nombre + 1):
        if nombre % i == 0:
            facteurs.add(i)
    return facteurs


# Kasiki Examination Fontion
def examen_kasiski(chemin_fichier, seuil_certitude=3):
    # Lire le texte du fichier
    texte = lire_fichier(chemin_fichier)

    # Trouver les séquences répétées dans le texte
    sequences_repetees = trouver_sequences_repetees(texte)

    # Calculer les distances entre les séquences répétées
    distances = calculer_distances(sequences_repetees)

    # Si aucune distance trouvée, retourner ?
    if not distances:
        return "?"

    # Trier les distances par longueur de séquence
    distances.sort(key=lambda x: len(x[0]), reverse=True)

    # Prendre la première ligne de la table
    premiere_ligne = distances[0]
    seq, distance = premiere_ligne

    # Calculer les facteurs de la distance
    candidats = trouver_facteurs(distance)

    # Si aucun facteur trouvé, retourner ?
    if not candidats:
        return "?"

    # Parcourir les autres lignes de la table
    for seq, distance in distances:
        temp = []
        for candidat in candidats:
            gcd_value = gcd(candidat, distance)
            if gcd_value != 1:
                temp.append(gcd_value)

        # Si des facteurs communs trouvés, mettre à jour les candidats
        if temp:
            candidats = temp
        # Si temp est vide et il reste des lignes, continuer
        elif not temp and distances.index((seq, distance)) < len(distances) - 1:
            continue
        # Si temp est vide et il n'y a plus de lignes, sortir
        elif not temp:
            break

    # Si aucun facteur commun trouvé, retourner ?
    if not candidats:
        return "?"

    # Determiner la taille potentielle de la clé
    taille_potentielle_clef = min(candidats)

    # Determiner la certitude
    certitude = len(candidats) >= seuil_certitude

    # Retourner la taille potentielle de la clé
    return f"{taille_potentielle_clef}{' ?' if not certitude else ''}"