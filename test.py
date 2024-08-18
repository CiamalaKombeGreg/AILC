import unittest
import os
import csv
import sys
from datetime import datetime
from pervision import File


class TestFile(unittest.TestCase):

    # Data de test
    file = File("test", datetime(2024, 3, 28), datetime(2020, 8, 10), "1658")

    def re_analyse(self, chemin, fichier):
        if os.path.exists(chemin) is False:  # On vérifie si le répertoire existe
            return "No directory"

        # Vérifier si c'est un fichier
        if os.path.isfile(f"{chemin}\{fichier}"):
            # Récupérer les métadonnées
            taille = os.path.getsize(f"{chemin}\{fichier}")  # Taille en octets
            return [fichier, taille]

        return "Not a file"

    def delfile(self, cles, repertoire):
        """On efface tous les cle qui ne sont pas trouvé dans le répertoire comme fichier"""
        fichiers = cles - repertoire
        return fichiers

    # tests

    def test_creation(self):
        """On teste la création de cette classe"""
        self.assertEqual(self.file.nom, "test")
        self.assertEqual(self.file.datec, datetime(2024, 3, 28))
        self.assertEqual(self.file.datem, datetime(2020, 8, 10))
        self.assertEqual(self.file.taille, "1658")

    def test_set(self):
        """On teste les setter de la classe"""
        self.file.nom = "changer"
        self.file.datec = datetime(2024, 5, 12)
        self.file.datem = datetime(2021, 11, 7)
        self.file.taille = "5841"

        self.assertEqual(self.file.nom, "changer")
        self.assertEqual(self.file.datec, datetime(2024, 5, 12))
        self.assertEqual(self.file.datem, datetime(2021, 11, 7))
        self.assertEqual(self.file.taille, "5841")

    def test_analyse(self):
        """On va tester si on récupère les bonnes informations"""
        self.assertEqual(self.re_analyse("testdirectory", "testfile"), ["testfile", 5])
        self.assertEqual(self.re_analyse("fztf", "testfile"), "No directory")
        self.assertEqual(self.re_analyse("testdirectory", "notfile"), "Not a file")

    def test_delete(self):
        """Tous les fichiers qui ne sont pas dans le répertoires, seront effacer"""
        self.assertEqual(
            self.delfile({"file1", "file2", "file3", "file4"}, {"file3", "file4"}),
            {"file1", "file2"},
        )
        self.assertEqual(self.delfile({"file3", "file4"}, {"file3", "file4"}), set())


if __name__ == "__main__":
    unittest.main()
