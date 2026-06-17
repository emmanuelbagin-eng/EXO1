import random

# Génère un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)
nombre_essais = 0

print("Bienvenue dans le jeu Guess the Number !")
print("J'ai choisi un nombre entre 1 et 100. Essaie de le deviner.")

essai = None

while essai != nombre_secret:
    proposition = input("Propose un nombre : ")

    if not proposition.isdigit():
        print("Merci d'entrer un nombre valide.")
        continue

    essai = int(proposition)
    nombre_essais = nombre_essais + 1

    if essai < nombre_secret:
        print("Trop petit !")
    elif essai > nombre_secret:
        print("Trop grand !")
    else:
        print("Bravo ! Tu as trouvé le nombre " + str(nombre_secret) + " en " + str(nombre_essais) + " essais.")
