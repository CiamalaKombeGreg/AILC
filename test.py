import unittest
import os
from datetime import datetime
from pervision import File


class TestFile(unittest.TestCase):

    # Data de test
    file = File("test", datetime(2024, 3, 28), datetime(2020, 8, 10), "1658")

    def test_creation(self):
        """On teste la création de cette classe"""
        self.assertEqual(self.file.nom, "test")
        self.assertEqual(self.file.datec, datetime(2024, 3, 28))
        self.assertEqual(self.file.datem, datetime(2020, 8, 10))
        self.assertEqual(self.file.taille, "1658")


if __name__ == "__main__":
    unittest.main()
