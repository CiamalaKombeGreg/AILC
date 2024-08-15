# Librairies
"""
    Toutes les librairies et importations utilisées
"""

import os
import csv
from datetime import datetime

# Variables

files = {}  # Les classes files seront encodées dans cette variable

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
        return f"Le fichier {self.__nom}, crée le {self.__datec} et modifié le {self.__datem} a eût une taille de {self.__taille}."

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
            files[nom_fichier] = File(
                nom_fichier, date_creation, date_modification, taille
            )

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
    except IOError as e:
        print("Une erreur de fichier est intervenue :" + e)
