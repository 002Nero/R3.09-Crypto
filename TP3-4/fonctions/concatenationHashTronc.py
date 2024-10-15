import hashlib
import base64
import os

MASTER_PASSWORD_FILE = '../fichier/mpwd.txt'

def get_master_password():
    if os.path.exists(MASTER_PASSWORD_FILE):
        with open(MASTER_PASSWORD_FILE, 'r') as file:
            master_password = file.read().strip()
            if master_password:
                return master_password

    return set_new_master_password()

def set_new_master_password():
    while True:
        master_password = input("Entrez un nouveau mot de passe maître (sans espaces) : ").strip()
        if ' ' in master_password:
            print("Le mot de passe maître ne doit pas contenir d'espaces.")
        else:
            with open(MASTER_PASSWORD_FILE, 'w') as file:
                file.write(master_password)
            return master_password

def hacher_et_troncer(master_password, str2, N):
    if not (1 <= N <= 12):
        raise ValueError("N doit être compris entre 1 et 12")

    string_concatener = master_password + str2
    hash_objet = hashlib.sha512(string_concatener.encode())
    hash_bytes = hash_objet.digest()
    base64_hash = base64.b64encode(hash_bytes).decode('ascii')[:N]
    return base64_hash

def main():
    change_password = input("Voulez-vous changer le mot de passe maître ? (oui/non) : ").strip().lower()
    if change_password == 'oui':
        master_password = set_new_master_password()
    else:
        master_password = get_master_password()

    str2 = input("Entrez la chaîne de caractères : ").strip()

    while True:
        try:
            N = int(input("Entrez la taille du mot de passe attendu (1-12) : ").strip())
            if not (1 <= N <= 12):
                raise ValueError
            break
        except ValueError:
            print("N doit être compris entre 1 et 12. Veuillez réessayer.")

    result = hacher_et_troncer(master_password, str2, N)
    print(f"Mot de passe généré : {result}")

if __name__ == "__main__":
    main()