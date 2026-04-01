from pymongo import MongoClient
from models import Entity

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "jeu_cli"
COL_CHARACTERS = "characters"
COL_MONSTERS = "monsters"
COL_SCORES = "scores"
TEAM_SIZE = 3
TOP_N = 3

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


# Affiche un message et demande une saisie d'un nombre entre mini et maxi.
def saisir_choix(mini, maxi):
    while True:
        entree = input("Ton choix (" + str(mini) + "-" + str(maxi) + ") : ")
        if entree.isdigit() and mini <= int(entree) <= maxi:
            return int(entree)
        print("Choix invalide, entre un nombre entre {} et {}.".format(mini, maxi))


# recuperer un pseudo pas trop court.
def saisir_pseudo():
    while True:
        txt = input("Entre ton pseudo : ").strip()
        if len(txt) >= 2:
            return txt
        print("Le pseudo doit faire au moins 2 caracteres.")


# Affiche les persos numerotes pour faciliter le choix.
def afficher_personnages(liste):
    print("\n--- Personnages disponibles ---")
    for i, p in enumerate(liste):
        print("  {}) {} (ATK:{} DEF:{} HP:{})".format(i + 1, p.name, p.attack, p.defense, p.hp))


def afficher_equipe(equipe):
    print("\n--- Ton equipe ---")
    for p in equipe:
        print("  - {} (ATK:{} DEF:{} HP:{})".format(p.name, p.attack, p.defense, p.hp))


def afficher_top3(scores):
    print("\n+----------------------------+")
    print("|   TOP 3 MEILLEURS SCORES   |")
    print("+----------------------------+")
    if not scores:
        print("  Aucun score enregistre.")
        return
    for i, row in enumerate(scores):
        print("  {}. {} - {} vagues".format(i + 1, row["username"], row["waves"]))


 # Convertit un document MongoDB en objet Entity.
def _mk_ent(doc, kind):
    return Entity(doc["name"], doc["attack"], doc["defense"], doc["hp"], kind)


# lire tous les persos, puis les mapper en Entity.
def get_chars():
    docs = db[COL_CHARACTERS].find()
    out = []
    for d in docs:
        out.append(_mk_ent(d, "character"))
    return out

# prendre un monstre aleatoire dans la base, puis le mapper en Entity.
def pick_monster():
    lst = list(db[COL_MONSTERS].aggregate([{"$sample": {"size": 1}}]))
    d = lst[0]
    return _mk_ent(d, "monster")

# Sauvegarde le score de la partie.
def save_score(username, waves):
    db[COL_SCORES].insert_one({"username": username, "waves": waves})


#trier par vagues descendantes et limiter a TOP 3
def get_top():
    res = db[COL_SCORES].find().sort("waves", -1).limit(TOP_N)
    return list(res)


# compat imports ailleurs
get_all_characters = get_chars
get_random_monster = pick_monster
get_top3 = get_top
