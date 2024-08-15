# Librairies
"""
    Toutes les librairies et importations utilisées
"""

import os
import csv
from datetime import datetime

# Variables

files = []

# Classes


class file:
    def __init__(self, nom, dateC, dateM, taille):
        self.__nom = nom
        self.__datec = dateC
        self.__datem = dateM
        self.__taille = taille

    def __str__(self):
        return f"Le fichier {self.__nom}, crée le {self.__datec} et modifié le {self.__datem} a eût une taille de {self.__taille}."

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, new_nom):
        self.__nom = new_nom

    @property
    def datec(self):
        return self.__datec

    @datec.setter
    def datec(self, new_date):
        self.__datec = new_date

    @property
    def datem(self):
        return self.__datem

    @datem.setter
    def datem(self, new_date):
        self.__datem = new_date

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, new_taille):
        self.__taille = new_taille


# Fonctions


def analyse(chemin):
    """analyse les fichiers du répertoire choisi et encode les métadonnées dans le fichier CSV

    PRE : Prend le chemin du répertoire comme paramètre 'chemin'

    POST : Retranscrit les métadonnées (nom, date de création, date
           de mise à jour et taille) de tous les fichiers dans un fichier CSV

    RAISE :
    """

    # Parcourir les fichiers dans le répertoire
    for nom_fichier in os.listdir(chemin):
        chemin_fichier = os.path.join(chemin, nom_fichier)

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
            files.append(file(nom_fichier, date_creation, date_modification, taille))

    try:
        with open("meta.csv", "w", newline="", encoding="utf-8") as csvfile:
            spamwriter = csv.writer(
                csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            for f in files:
                spamwriter.writerow([f.nom, f.datec, f.datem, f.taille])
    except FileNotFoundError as e:
        print("Le fichier n'as pas été trouvée :" + e)
    except IOError as e:
        print("Une erreur de fichier est intervenue :" + e)
