# Librairies
"""
    Toutes les librairies et importations utilisées
"""

import os
import cmd
import sys
from pervision import analyse

# classe


def cls():
    """
    Cette fonction permet de clear la l'interface en ligne de commande
    """
    os.system("cls" if os.name == "nt" else "clear")


class mainProg(cmd.Cmd):
    cls()
    analyse(sys.argv[1])
    intro = "Pervision 1.0   Tapez help ou ? to pour afficher la liste des commandes.\n"
    prompt = sys.argv[1] + " > "
    file = None

    # ----- basic enquete commands -----

    def do_pervision(self, arg):
        "\n{logs} - Afficher le fichier log.\n\n{fichiers} - Afficher les fichiers.\n"

        cls()
        if arg == "logs":
            print("logs")
        elif arg == "fichiers":
            print("fichiers")
        else:
            print(
                "Argument erroné, faites <help pervision> pour plus d'informations.\n"
            )

    def do_ls(self, arg):
        "Afficher le répertoire"

        cls()
        print(os.system("dir " + sys.argv[1]))

    def do_fermer(self, arg):
        "Ferme le programme"

        cls()
        print("Merci et à bientôt!")
        return True


# Corps principale

if __name__ == "__main__":
    if (
        len(sys.argv) == 2
    ):  # On verifie si il n'y a que deux argument, l'application et le chemin du répertoire
        if os.path.exists(sys.argv[1]):  # On verifie que le réperoire existe
            if os.path.isdir(
                sys.argv[1]
            ):  # On verifie si nous avons bien un répertoire
                mainProg().cmdloop()
            else:
                print("Ce n'est pas un répertoire.")
        else:
            print("Ce répertoire n'existe pas.")
    else:
        print("Nombre d'argument érronée (ex. python main.py [chemin du répertoire])")
