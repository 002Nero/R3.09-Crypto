import re
from collections import defaultdict
from math import gcd
from functools import reduce
    # Fonction qui permet de lire un fichier
def lire_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        return fichier.read()

    # Fonction qui permet de trouver les séquences répétées dans un texte
def trouver_sequences_repetees(texte, longueur_sequence=3):
    sequences = defaultdict(list)
    for i in range(len(texte) - longueur_sequence + 1):
        seq = texte[i:i + longueur_sequence]
        sequences[seq].append(i)
    return {seq: indices for seq, indices in sequences.items() if len(indices) > 1}

def calculer_distances(sequences_repetees):
    distances = []
    for indices in sequences_repetees.values():
        for i in range(len(indices) - 1):
            distances.append(indices[i + 1] - indices[i])
    return distances

def trouver_facteurs(nombre):
    facteurs = set()
    for i in range(2, nombre + 1):
        if nombre % i == 0:
            facteurs.add(i)
    return facteurs

def examen_kasiski(chemin_fichier, seuil_certitude=3):
    # Lire le texte chiffré à partir du fichier
    texte = lire_fichier(chemin_fichier)

    # Trouver les séquences répétées dans le texte
    sequences_repetees = trouver_sequences_repetees(texte)

    # Calculer les distances entre les séquences répétées
    distances = calculer_distances(sequences_repetees)

    if not distances:
        return None

    # Trouver les facteurs communs des distances
    facteurs_communs = reduce(lambda x, y: x & y, (trouver_facteurs(distance) for distance in distances))

    if not facteurs_communs:
        return None

    # Déterminer la taille potentielle de la clé
    taille_potentielle_clef = min(facteurs_communs)

    # Vérifier le nombre de facteurs communs pour la certitude
    certitude = len(facteurs_communs) >= seuil_certitude

    # Retourner la taille potentielle de la clé avec un ? si incertain
    return f"{taille_potentielle_clef}{' ?' if not certitude else ''}"