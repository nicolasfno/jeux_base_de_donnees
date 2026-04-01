class Entity:
    def __init__(self, name, attack, defense, hp, type_entite):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.type_entite = type_entite  # "character" ou "monster"
