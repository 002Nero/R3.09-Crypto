import hashlib
import base64


def hacher_et_troncer(str1, str2, tailleMdp):
    # Vérifier que tailleMdp est dans la plage valide
    if not (1 <= tailleMdp <= 120):
        raise ValueError("tailleMdp doit être compris entre 1 et 12")

    # Concatenation de deux chaines de caractères
    string_concatener = str1 + str2

    # Hachage de la chaine de caractères
    hash_objet = hashlib.sha512(string_concatener.encode())
    hash_bytes = hash_objet.digest()

    # Convertir le hash en Base64 et tronquer à tailleMdp caractères
    base64_hash = base64.b64encode(hash_bytes).decode('ascii')[:tailleMdp]

    # Retourner le hash tronqué en ASCII
    return base64_hash

# Example usage
str1 = "/njkj[p[kjjkofdasmbjskldfhejwqkldvbfuiowdvgfswpoifhdjewkdsngiy3uejdscnbfjriueodjsck"
str2 = "fdsDW2345+-*-/-*//*-//*-*/4-45*4*fdhaejgydhusjdkabsgetuidjskcbshreuwidjsksreyuiwdsjvbrhkyui-"
tailleMdp = 60
result = hacher_et_troncer(str1, str2, tailleMdp)
print(result)