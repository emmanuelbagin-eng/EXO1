import random

# Génère un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

print("Bienvenue dans le jeu 'Guess the Number' !")
print("J'ai choisi un nombre entre 1 et 100. Essaie de le deviner.")

essai = None

while essai != nombre_secret:
    # Récupère la proposition de l'utilisateur
    proposition = input("Propose un nombre : ")

    # Vérifie que l'utilisateur a bien tapé un nombre
    if not proposition.isdigit():
        print("Merci d'entrer un nombre valide.")
        continue

    essai = int(proposition)

    if essai < nombre_secret:
        print("Trop petit !")
    elif essai > nombre_secret:
        print("Trop grand !")
    else:
        print(f"Bravo ! Tu as trouvé le nombre {nombre_secret} !")
