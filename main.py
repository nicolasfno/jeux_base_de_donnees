from db_init import initialiser_db
from game import choisir_equipe, boucle_vagues
from utils import (
    saisir_choix,
    saisir_pseudo,
    afficher_top3,
    save_score,
    get_top3,
)


def menu_principal():
    while True:
        print("\n\n====================================")
        print("  RPG MONGODB - MENU PRINCIPAL")
        print("====================================")
        print("  1) Demarrer le jeu")
        print("  2) Afficher le classement")
        print("  3) Quitter")

        choix = saisir_choix(1, 3)

        if choix == 1:
            demarrer_partie()
        elif choix == 2:
            afficher_top3(get_top3())
        else:
            print("A bientot !")
            break


def demarrer_partie():
    pseudo = saisir_pseudo()
    print(f"\nBienvenue {pseudo} ! Choisis ton equipe.\n")

    equipe = choisir_equipe()
    vagues = boucle_vagues(equipe)

    save_score(pseudo, vagues)
    print(f"\n{pseudo}, tu as survecu {vagues} vagues !")
    afficher_top3(get_top3())


if __name__ == "__main__":
    initialiser_db()
    menu_principal()
