# Ce fichier contient des classes et fonctions de base pour le jeu.
class Entity:
    def __init__(self, name, attack, defense, hp, type_entite):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        # type_entite sert surtout a savoir d'ou vient l'entite.
        self.type_entite = type_entite  # "character" ou "monster"
