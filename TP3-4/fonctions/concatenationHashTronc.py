import hashlib
import base64

def hacher_et_troncer(str1, str2):
    # Concatenation de deux chaines de caractères
    string_concatener = str1 + str2

    # Hachage de la chaine de caractères
    hash_objet = hashlib.sha256(string_concatener.encode())
    hash_bytes = hash_objet.digest()

    # Convertir le hash en Base64 et tronquer à 8 caractères
    base64_hash = base64.b64encode(hash_bytes).decode('ascii')[:8]

    # Retourner le hash tronqué en ASCII
    return base64_hash

# Example usage
str1 = "/*/**/*-/*/*/-555*/"
str2 = "fdsDW2345+-*-/-*//*-//*-*/4-45*4*-"
result = hacher_et_troncer(str1, str2)
print(result)