import random
import time
from utils import (
    afficher_personnages,
    afficher_equipe,
    saisir_choix,
    get_chars,
    pick_monster,
    TEAM_SIZE,
)

# charger les persos dispo depuis la base.
def choisir_equipe():
    persos = get_chars()
    team = []

# laisser joueur choisir un persos et retire le perso choisi pour eviter les doublons.
    while len(team) < TEAM_SIZE:
        print("\nChoix {}/{}".format(len(team) + 1, TEAM_SIZE))
        afficher_personnages(persos)
        c = saisir_choix(1, len(persos))  
        p = persos.pop(c - 1)
        team.append(p)
        afficher_equipe(team)

    return team

# Calcul des degats d'une attaque.
def calculer_degats(attaquant, defenseur):
    val = max(1, attaquant.attack - defenseur.defense)
    return val


# Garde seulement les persos avec HP > 0.
def vivants(equipe):
    return [p for p in equipe if p.hp > 0]


# tous les persos vivants attaquent le monstre.
def tour(equipe, monstre):
    for perso in vivants(equipe):
        time.sleep(0.6)
        degats = calculer_degats(perso, monstre)
        monstre.hp -= degats
        print(f"  {perso.name} inflige {degats} degats a {monstre.name} (HP: {max(0, monstre.hp)})")
        if monstre.hp <= 0:
            time.sleep(0.4)
            print(f"  >>> {monstre.name} est vaincu !")
            return True

# si le monstre est encore vivant, il contre-attaque.
    team_ok = vivants(equipe)
    if team_ok:
        time.sleep(0.8)
        cible = random.choice(team_ok)
        degats = calculer_degats(monstre, cible)
        cible.hp -= degats
        print(f"  {monstre.name} inflige {degats} degats a {cible.name} (HP: {max(0, cible.hp)})")

    return False

 # Compteur de vagues
def boucle_vagues(equipe):
    n = 0

# Tant qu'il reste au moins un perso vivant, on continue.
    while vivants(equipe):
        n += 1
        
# choisir un monstre aleatoire pour cette vague.
        monstre = pick_monster()
        print("\n====== VAGUE {} : {} apparait ! (HP:{}) ======".format(n, monstre.name, monstre.hp))
        time.sleep(1)

# jouer des tours jusqu'a victoire/defaite de la vague.
        while monstre.hp > 0 and vivants(equipe):
            monstre_vaincu = tour(equipe, monstre)
            if monstre_vaincu:
                break
        time.sleep(0.5)

# plus de persos vivants -> fin de partie.
    print("\n*** GAME OVER apres {} vagues ! ***".format(n))
    return n
