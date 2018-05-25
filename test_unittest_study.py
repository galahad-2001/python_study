import unittest
from unittest_study import Aclass


class AclassTest(unittest.TestCase):
    """docstring for ClassName"""

    def test_aclass(self):
        s = Aclass()
        name = s.name
        self.assertEqual(s.name, "test")

    def test_aclass2(self):
        s = Aclass("Jayden")
        name = s.name
        self.assertEqual(s.name, "Jayden")


unittest.main()
