import random
import time
from utils import (
    afficher_personnages,
    afficher_equipe,
    saisir_choix,
    get_all_characters,
    get_random_monster,
    TEAM_SIZE,
)


def choisir_equipe():
    personnages = get_all_characters()
    equipe = []

    while len(equipe) < TEAM_SIZE:
        print(f"\nChoix {len(equipe) + 1}/{TEAM_SIZE}")
        afficher_personnages(personnages)
        choix = saisir_choix(1, len(personnages))
        perso = personnages.pop(choix - 1)
        equipe.append(perso)
        afficher_equipe(equipe)

    return equipe


def calculer_degats(attaquant, defenseur):
    # Evite les combats bloques quand la defense est >= a l'attaque.
    degats = max(1, attaquant.attack - defenseur.defense)
    return degats


def entites_vivantes(equipe):
    return [p for p in equipe if p.hp > 0]


def jouer_tour(equipe, monstre):
    for perso in entites_vivantes(equipe):
        time.sleep(0.6)
        degats = calculer_degats(perso, monstre)
        monstre.hp -= degats
        print(f"  {perso.name} inflige {degats} degats a {monstre.name} (HP: {max(0, monstre.hp)})")
        if monstre.hp <= 0:
            time.sleep(0.4)
            print(f"  >>> {monstre.name} est vaincu !")
            return True

    vivants = entites_vivantes(equipe)
    if vivants:
        time.sleep(0.8)
        cible = random.choice(vivants)
        degats = calculer_degats(monstre, cible)
        cible.hp -= degats
        print(f"  {monstre.name} inflige {degats} degats a {cible.name} (HP: {max(0, cible.hp)})")

    return False


def boucle_vagues(equipe):
    vagues = 0

    while entites_vivantes(equipe):
        vagues += 1
        monstre = get_random_monster()
        print(f"\n====== VAGUE {vagues} : {monstre.name} apparait ! (HP:{monstre.hp}) ======")
        time.sleep(1)

        while monstre.hp > 0 and entites_vivantes(equipe):
            monstre_vaincu = jouer_tour(equipe, monstre)
            if monstre_vaincu:
                break
        time.sleep(0.5)

    print(f"\n*** GAME OVER apres {vagues} vagues ! ***")
    return vagues
