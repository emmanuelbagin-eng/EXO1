import random  # module qui permet de générer des nombres aléatoires

# === INITIALISATION DU JEU ===
# Génère un nombre aléatoire entre 1 et 100 (inclus)
nombre_secret = random.randint(1, 100)

print("Bienvenue dans le jeu 'Guess the Number' !")
print("J'ai choisi un nombre entre 1 et 100. Essaie de le deviner.")

# Variable qui stockera la proposition de l'utilisateur
# Initialisée à None pour forcer le premier tour de boucle
essai = None

# === BOUCLE PRINCIPALE DU JEU ===
# Continue tant que l'utilisateur n'a pas trouvé le bon nombre
while essai != nombre_secret:
    # Récupère la proposition de l'utilisateur (toujours sous forme de texte)
    proposition = input("Propose un nombre : ")

    # Vérification : on s'assure que l'utilisateur a bien tapé un nombre
    if not proposition.isdigit():
        print("Merci d'entrer un nombre valide.")
        continue

    # Conversion du texte en nombre entier pour pouvoir le comparer
    essai = int(proposition)

    # === COMPARAISON AVEC LE NOMBRE SECRET ===
    if essai < nombre_secret:
        print("Trop petit !")
    elif essai > nombre_secret:
        print("Trop grand !")
    else:
        print(f"Bravo ! Tu as trouvé le nombre {nombre_secret} !")
