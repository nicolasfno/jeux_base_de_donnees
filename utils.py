from pymongo import MongoClient
import random

# --- Constantes ---
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "jeu_cli"
COL_CHARACTERS = "characters"
COL_MONSTERS = "monsters"
COL_SCORES = "scores"
TEAM_SIZE = 3
TOP_N = 3

# --- Connexion MongoDB ---
client = MongoClient(MONGO_URI)
db = client[DB_NAME]


# --- Fonctions de saisie ---

def saisir_choix(mini, maxi):
    while True:
        entree = input(f"Ton choix ({mini}-{maxi}) : ")
        if entree.isdigit() and mini <= int(entree) <= maxi:
            return int(entree)
        print(f"Choix invalide, entre un nombre entre {mini} et {maxi}.")


def saisir_pseudo():
    while True:
        pseudo = input("Entre ton pseudo : ").strip()
        if len(pseudo) >= 2:
            return pseudo
        
        print("Le pseudo doit faire au moins 2 caracteres.")


# --- Fonctions d'affichage ---

def afficher_personnages(liste):
    print("\n--- Personnages disponibles ---")
    for i, perso in enumerate(liste):
        print(f"  {i +1}) {perso.name} (ATK:{perso.attack} DEF:{perso.defense} HP:{perso.hp})")


def afficher_equipe(equipe):
    print("\n--- Ton equipe ---")
    for perso in equipe:
        print(f"  - {perso.name} (ATK:{perso.attack} DEF:{perso.defense} HP:{perso.hp})")


def afficher_top3(scores):
    print("\n+----------------------------+")
    print("|   TOP 3 MEILLEURS SCORES   |")
    print("+----------------------------+")
    if not scores:
        print("  Aucun score enregistre.")
        return
    for i, s in enumerate(scores):
        print(f"  {i + 1}. {s['username']} - {s['waves']} vagues")


# --- Fonctions MongoDB ---

def get_all_characters():
    from models import Entity
    docs = db[COL_CHARACTERS].find()
    return [Entity(doc["name"], doc["attack"], doc["defense"], doc["hp"], "character") for doc in docs]


def get_random_monster():
    from models import Entity
    pipeline = [{"$sample": {"size": 1}}]
    docs = list(db[COL_MONSTERS].aggregate(pipeline))
    doc = docs[0]
    return Entity(doc["name"], doc["attack"], doc["defense"], doc["hp"], "monster")


def save_score(username, waves):
    db[COL_SCORES].insert_one({"username": username, "waves": waves})


def get_top3():
    docs = db[COL_SCORES].find().sort("waves", -1).limit(TOP_N)
    return list(docs)
