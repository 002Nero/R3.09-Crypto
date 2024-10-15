import hashlib
import base64
import itertools
import string

MASTER_PASSWORD_FILE = '../fichier/mpwd.txt'

def hacher_et_troncer(master_password, str2, N):
    if not (1 <= N <= 12):
        raise ValueError("N doit être compris entre 1 et 12")

    string_concatener = master_password + str2
    hash_objet = hashlib.sha512(string_concatener.encode())
    hash_bytes = hash_objet.digest()
    base64_hash = base64.b64encode(hash_bytes).decode('ascii')[:N]
    return base64_hash

def generate_passwords_for_tags(master_password):
    tags = ["Unilim", "Amazon", "Netflix"]
    N = 1
    passwords = {tag: hacher_et_troncer(master_password, tag, N) for tag in tags}
    return passwords

def dictionary_attack(target_password, tag, N=1):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    attempts = 0

    # Itérer sur toutes les combinaisons possibles de mots de passe de 10 caractères
    for candidate in itertools.product(characters, repeat=10):
        candidate_password = ''.join(candidate)
        generated_password = hacher_et_troncer(candidate_password, tag, N)
        attempts += 1
        if generated_password == target_password:
            return candidate_password, attempts

    return None, attempts

# Étape 1 : S'assurer que le fichier de mot de passe maître contient un mot de passe maître de 10 caractères
with open(MASTER_PASSWORD_FILE, 'w') as file:
    master_password = 'sdfghjkl;p'
    file.write(master_password)

# Étape 2 : Générer des mots de passe pour les tags
passwords = generate_passwords_for_tags(master_password)
print("Mots de passe générés pour les tags :", passwords)

# Étape 3 : Effectuer une attaque par dictionnaire pour le tag "Unilim"
target_password = passwords["Unilim"]
found_password, attempts = dictionary_attack(target_password, "Unilim")

if found_password:
    print(f"Mot de passe maître trouvé : {found_password} en {attempts} tentatives")
else:
    print("Mot de passe maître non trouvé")