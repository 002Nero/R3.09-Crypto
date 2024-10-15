import hashlib
import base64


def hacher_et_troncer(str1, str2, N):
    # Vérifier que N est dans la plage valide
    if not (1 <= N <= 12):
        raise ValueError("N doit être compris entre 1 et 12")

    # Concatenation de deux chaines de caractères
    string_concatener = str1 + str2

    # Hachage de la chaine de caractères
    hash_objet = hashlib.sha512(string_concatener.encode())
    hash_bytes = hash_objet.digest()

    # Convertir le hash en Base64 et tronquer à N caractères
    base64_hash = base64.b64encode(hash_bytes).decode('ascii')[:N]

    # Retourner le hash tronqué en ASCII
    return base64_hash


# Jeux d'essais
def jeux_d_essais():
    essais = [
        ("/njkj[p[kjjkofdasmbjskldfhejwqkldvbfuiowdvgfswpoifhdjewkdsngiy3uejdscnbfjriueodjsck",
         "fdsDW2345+-*-/-*//*-//*-*/4-45*4*fdhaejgydhusjdkabsgetuidjskcbshreuwidjsksreyuiwdsjvbrhkyui-", 8),
        ("Hello", "World", 5),
        ("123", "456", 12),
        ("abc", "def", 1),
        ("", "", 10),  # Cas de test avec des chaînes vides
        ("special*&^%$", "characters!@#", 6),
        ("Hello", "World", 14),
        ("Hello", "World", 0)  # Cas de test avec N = 0
    ]

    for str1, str2, N in essais:
        try:
            result = hacher_et_troncer(str1, str2, N)
            print(f"Input: ({str1}, {str2}, {N}) => Output: {result}")
        except ValueError as e:
            print(f"Input: ({str1}, {str2}, {N}) => Error: {e}")


jeux_d_essais()