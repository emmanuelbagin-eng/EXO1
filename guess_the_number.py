import random

# Parametres du jeu
nombre_secret = random.randint(1, 100)
nombre_essais = 0
max_essais = 10

print("Bienvenue dans le jeu Guess the Number !")
print("J'ai choisi un nombre entre 1 et 100. Tu as " + str(max_essais) + " essais pour le trouver.")

essai = None

# Boucle principale
while essai != nombre_secret and nombre_essais < max_essais:
    proposition = input("Propose un nombre : ")

    if not proposition.isdigit():
        print("Merci d'entrer un nombre valide.")
        continue

    essai = int(proposition)
    nombre_essais = nombre_essais + 1

    if essai < nombre_secret:
        print("Trop petit !")
        if nombre_secret - essai <= 5:
            print("Tu es tout proche !")
    elif essai > nombre_secret:
        print("Trop grand !")
        if essai - nombre_secret <= 5:
            print("Tu es tout proche !")
    else:
        if nombre_essais == 1:
            print("Bravo ! Tu as trouvé le nombre " + str(nombre_secret) + " en 1 essai.")
        else:
            print("Bravo ! Tu as trouvé le nombre " + str(nombre_secret) + " en " + str(nombre_essais) + " essais.")

if essai != nombre_secret:
    print("Dommage, tu as utilisé tous tes essais. Le nombre était " + str(nombre_secret) + ".")

rejouer = input("Veux-tu rejouer ? (oui/non) : ")
if rejouer.lower() == "oui":
    print("Relance le programme pour rejouer.")
