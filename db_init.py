from utils import db, COL_CHARACTERS, COL_MONSTERS, COL_SCORES

PERSONNAGES = [
    {"name": "Guerrier", "attack": 15, "defense": 10, "hp": 100},
    {"name": "Mage", "attack": 20, "defense": 5, "hp": 80},
    {"name": "Archer", "attack": 18, "defense": 7, "hp": 90},
    {"name": "Voleur", "attack": 22, "defense": 8, "hp": 85},
    {"name": "Paladin", "attack": 14, "defense": 12, "hp": 110},
    {"name": "Sorcier", "attack": 25, "defense": 3, "hp": 70},
    {"name": "Chevalier", "attack": 17, "defense": 15, "hp": 120},
    {"name": "Moine", "attack": 19, "defense": 9, "hp": 95},
    {"name": "Berserker", "attack": 23, "defense": 6, "hp": 105},
    {"name": "Chasseur", "attack": 16, "defense": 11, "hp": 100}
]

MONSTRES = [
    {"name": "Gobelin", "attack": 10, "defense": 5, "hp": 50},
    {"name": "Orc", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Dragon", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Zombie", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Troll", "attack": 25, "defense": 15, "hp": 200},
    {"name": "Spectre", "attack": 18, "defense": 10, "hp": 100},
    {"name": "Golem", "attack": 30, "defense": 25, "hp": 250},
    {"name": "Vampire", "attack": 22, "defense": 12, "hp": 150},
    {"name": "Loup-garou", "attack": 28, "defense": 18, "hp": 180},
    {"name": "Squelette", "attack": 15, "defense": 7, "hp": 90}
]


def initialiser_db():
    db[COL_CHARACTERS].drop()
    db[COL_MONSTERS].drop()

    db[COL_CHARACTERS].insert_many(PERSONNAGES)
    print(f"{len(PERSONNAGES)} personnages inseres.")

    db[COL_MONSTERS].insert_many(MONSTRES)
    print(f"{len(MONSTRES)} monstres inseres.")

    if COL_SCORES not in db.list_collection_names():
        db.create_collection(COL_SCORES)
        print("Collection scores creee.")

    print("Base de donnees initialisee avec succes !")


if __name__ == "__main__":
    initialiser_db()
