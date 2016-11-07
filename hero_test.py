import unittest
from hero import Hero


class Hero_test(unittest.TestCase):

    def setUp(self):
        self.super_gosho = Hero(name="Gosho", title="Ubiec", health=100, mana=100, mana_regeneration_rate=2)
        self.captain_america = Hero(name="America", title="Captain", health=10, mana=10, mana_regeneration_rate=1)

    def test_hero(self):
        self.assertEqual(Hero(name="Gosho", title="Ubiec", health=100, mana=100, mana_regeneration_rate=2), self.super_gosho)
        self.assertEqual(Hero(name="America", title="Captain", health=10, mana=10, mana_regeneration_rate=1), self.captain_america)


if __name__ == "__main__":
    unittest.main()
