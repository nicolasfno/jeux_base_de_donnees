from db_init import initialiser_db
from game import choisir_equipe, boucle_vagues
from utils import (
    saisir_choix,
    saisir_pseudo,
    afficher_top3,
    save_score,
    get_top,
)

# afficher le menu tant
def menu():
    while True:
        print("\n\n====================================")
        print("  RPG MONGODB - MENU PRINCIPAL")
        print("====================================")
        print("  1) Demarrer le jeu")
        print("  2) Afficher le classement")
        print("  3) Quitter")

# recuperer le choix valide entre 1 et 3.
        c = saisir_choix(1, 3)

# lancer action selon le choix.
        if c == 1:
            run_game()
        elif c == 2:
            afficher_top3(get_top())
        else:
            print("A bientot !")
            break


# demander le pseudo.
def run_game():
    user = saisir_pseudo()
    print("\nBienvenue " + user + " ! Choisis ton equipe.\n")


# choisir l'equipe puis jouer les vagues.
    equipe = choisir_equipe()
    vagues = boucle_vagues(equipe)


# sauver et afficher le resultat final.
    save_score(user, vagues)
    print("\n{}, tu as survecu {} vagues !".format(user, vagues))
    afficher_top3(get_top())


# Point d'entree du programme.
if __name__ == "__main__":
    initialiser_db()
    menu()
