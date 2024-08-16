# Librairies
"""
    Toutes les librairies et importations utilisées
"""

import os
import cmd
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from pervision import analyse, afficher

# classe


def cls():
    """
    Cette fonction permet de clear la l'interface en ligne de commande
    """

    os.system("cls" if os.name == "nt" else "clear")


def any_event(event):
    """
    Cette fonction relance l'analyse des fichiers en cas d'évènements
    """

    analyse(sys.argv[1])


class Pervision(cmd.Cmd):
    """
    Cette classe lance un modèle cmd permettant de créer une interface en ligne de commande

    Cet ligne de commande peut utiliser des arguments et se manipule similairement à un shell
    """

    cls()
    intro = "Pervision 1.0   Tapez help ou ? to pour afficher la liste des commandes.\n"
    prompt = sys.argv[-1] + " > "
    file = None

    # ----- basic enquete commands -----

    def do_pervision(self, arg):
        "\n{analyse} - Analyser le répertoire.\n\n{fichiers} - Afficher les fichiers actuelles.\n"

        if arg == "analyse":
            cls()
            analyse(sys.argv[1])
        elif arg == "fichiers":
            cls()
            afficher()
        else:
            print(
                "Argument erroné, faites <help pervision> pour plus d'informations.\n"
            )

    def do_ls(self, arg):  # L'argument est nécessaire au bon fonctionnement
        "Afficher le répertoire"

        cls()
        print(os.system("dir " + sys.argv[1]))

    def do_cls(self, arg):  # L'argument est nécessaire au bon fonctionnement
        "Clear"

        cls()

    def do_fermer(self, arg):  # L'argument est nécessaire au bon fonctionnement
        "Ferme le programme"

        cls()
        print("Merci et à bientôt!")
        return True


# Corps principale

if __name__ == "__main__":
    # Initialiser le logging, la façon dont les logs seront encoder
    logging.basicConfig(
        filename="watchdog.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s -%(process)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if (
        len(sys.argv) == 2
    ):  # On verifie si il n'y a que deux argument, l'application et le chemin du répertoire
        if os.path.exists(sys.argv[1]):  # On verifie que le réperoire existe
            if os.path.isdir(sys.argv[1]):  # Un répertoire ?
                event_handler = LoggingEventHandler()
                event_handler.on_any_event = any_event
                observer = Observer()
                observer.schedule(event_handler, sys.argv[1], recursive=True)
                observer.start()
                Pervision().cmdloop()
                observer.stop()
            else:
                print("Ce n'est pas un répertoire.")
        else:
            print("Ce répertoire n'existe pas.")
    else:
        print("Nombre d'argument érronée (ex. python main.py [chemin du répertoire])")
