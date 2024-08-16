# Librairies
"""
    Toutes les librairies et importations utilisées
"""

import os
import csv
import sys
import time
from datetime import datetime

# Variables

files = {}  # Les classes files seront encodées dans cette variable

path = ""  # Chemin du répertoire

# Classes


class File:
    """
    Cette classe représente un fichier existant dans le répertoire choisi

    Ces fichiers permettront de comparer les changements présents dans le répertoires
    """

    def __init__(self, nom, datec, datem, taille):
        """
        Initialise une instance de la classe File.

        PRE : Aucune.
        POST : Crée un nouveau objet 'File' avec les informations spécifiées ...
        """

        self.__nom = nom
        self.__datec = datec
        self.__datem = datem
        self.__taille = taille

    def __str__(self):
        return f"Nom: {self.__nom} | Crée le {self.__datec} | Modifié le {self.__datem} | {self.__taille} octets."

    @property
    def nom(self):
        """Cette fonction retourne le nom de l'objet"""

        return self.__nom

    @nom.setter
    def nom(self, new_nom):
        """
        Modifie le nom de l'objet avec une nouvelle valeur.

        PRE : Aucune.
        POST :  Modifie le nom avec la nouvelle valeur...
        """

        self.__nom = new_nom

    @property
    def datec(self):
        """Cette fonction retourne la date de création de l'objet"""

        return self.__datec

    @datec.setter
    def datec(self, new_date):
        """
        Modifie la date de création de l'objet avec une nouvelle valeur.

        PRE : Aucune.
        POST :  Modifie la date de création avec la nouvelle valeur...
        """

        self.__datec = new_date

    @property
    def datem(self):
        """Cette fonction retourne la date de mise à jour de l'objet"""

        return self.__datem

    @datem.setter
    def datem(self, new_date):
        """
        Modifie la date de mise à jour de l'objet avec une nouvelle valeur.

        PRE : Aucune.
        POST :  Modifie la date de mise à jour avec la nouvelle valeur...
        """

        self.__datem = new_date

    @property
    def taille(self):
        """Cette fonction retourne la taille de l'objet"""

        return self.__taille

    @taille.setter
    def taille(self, new_taille):
        """
        Modifie la taille de l'objet avec une nouvelle valeur.

        PRE : Aucune.
        POST :  Modifie la taille avec la nouvelle valeur...
        """

        self.__taille = new_taille


# Fonctions


def analyse(chemin):
    """analyse les fichiers du répertoire choisi et encode les métadonnées dans le fichier CSV

    PRE : Prend le chemin du répertoire qui est valide comme paramètre 'chemin'

    POST : Retranscrit les métadonnées (nom, date de création, date
           de mise à jour et taille) de tous les fichiers dans un fichier CSV

    RAISE :
        - FileNotFoundError : Si le fichier CSV n'as pas été trouvée
        - IOError : Si tout problème concernant le fichier CSV a été trouvée
    """

    global path  # Ne détecte pas la variable path
    path = chemin

    if os.path.exists(sys.argv[1]) is False:  # On vérifie si le répertoire existe
        os.system("cls" if os.name == "nt" else "clear")
        # On va vider le fichier en l'ouvrant en écriture.
        try:
            with open("meta.csv", "w", newline="", encoding="utf-8") as csvfile:
                files.clear()
        except IOError as e:
            print("Le fichier CSV n'a pas pu être éffacer : " + e)
        print("Le répertoire est innaccesible.")
        return 0

    # Parcourir les fichiers dans le répertoire pour créer
    for nom in os.listdir(chemin):
        chemin_fichier = os.path.join(chemin, nom)

        # Vérifier si c'est un fichier
        if os.path.isfile(chemin_fichier):
            # Récupérer les métadonnées
            taille = os.path.getsize(chemin_fichier)  # Taille en octets
            date_creation = datetime.fromtimestamp(
                os.path.getctime(chemin_fichier)
            ).strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # Date de création
            date_modification = datetime.fromtimestamp(
                os.path.getmtime(chemin_fichier)
            ).strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # Date de mise à jour
            if nom in files.keys():
                files[nom].datem = date_modification
                files[nom].taille = taille
            else:
                files[nom] = File(nom, date_creation, date_modification, taille)

    # Effacer les fichiers n'existants plus
    delfile(set(files.keys()), set(os.listdir(chemin)))

    try:
        # On ouvre le fichier meta.csv en écriture
        with open("meta.csv", "w", newline="", encoding="utf-8") as csvfile:
            # On lie le contenu du fichier à un objet qui est représenter par uen variable
            spamwriter = csv.writer(
                csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            for f in files.items():
                # On encode les métadonnées des fichier, un fichier par ligne.
                spamwriter.writerow([f[1].nom, f[1].datec, f[1].datem, f[1].taille])
    except FileNotFoundError as e:
        print("Le fichier n'as pas été trouvée :" + e)
        exit()
    except IOError as e:
        print("Une erreur de fichier est intervenue :" + e)
        exit()


def delfile(cles, repertoire):
    """Prends en paramètres les clés du dicitonnaire et la liste des fichiers
        et les comparent pour éffacer les classes de fichiers inexistantes

    PRE : Aucunes.

    POST : Efface les clé-valeur du dictionnaire pour qui le fichier n'existe
            plus où à changer de nom
    """

    fichiers = cles - repertoire

    for i in fichiers:
        del files[i]


def afficher():
    """Affiche un tableau en ligne de commande avec les métadonnées des fichiers

    PRE : Aucunes.

    POST : Renvoie un tableau via des 'prints' avec les valeurs contenu dans les
            objets du dictionnaire 'fiches'
    """

    # Définir la largeur maximale pour chaque colonne
    largeur_colonnes = {
        "Nom": 30,
        "Date de création": 20,
        "Date de modification": 20,
        "Taille": 10,
    }

    # Afficher l'en-tête
    en_tete = (
        f"{'Nom'.ljust(largeur_colonnes['Nom'])} "
        f"{'Date de création'.ljust(largeur_colonnes['Date de création'])} "
        f"{'Date de modification'.ljust(largeur_colonnes['Date de modification'])} "
        f"{'Taille (octets)'.ljust(largeur_colonnes['Taille'])}"
    )
    print(en_tete)
    print("-" * sum(largeur_colonnes.values()))  # Ligne de séparation

    if not files:
        print("Répertoire vide...")

    for donnee in files.items():
        nom = donnee[1].nom[: largeur_colonnes["Nom"]]  # Tronquer si nécessaire
        date_creation = donnee[1].datec[: largeur_colonnes["Date de création"]]
        date_modification = donnee[1].datem[: largeur_colonnes["Date de modification"]]
        taille = str(donnee[1].taille)[: largeur_colonnes["Taille"]]

        ligne = (
            f"{nom.ljust(largeur_colonnes['Nom'])} "
            f"{date_creation.ljust(largeur_colonnes['Date de création'])} "
            f"{date_modification.ljust(largeur_colonnes['Date de modification'])} "
            f"{taille.ljust(largeur_colonnes['Taille'])}"
        )
        print(ligne)
    print("-" * sum(largeur_colonnes.values()))  # Ligne de séparation
