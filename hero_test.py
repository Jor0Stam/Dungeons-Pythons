import unittest
from hero import Hero
from weapons_spells import *


class Hero_test(unittest.TestCase):

    def setUp(self):
        self.super_gosho = Hero(name="Gosho", title="Ubiec", health=100, mana=100, mana_regeneration_rate=2)
        self.captain_america = Hero(name="America", title="Captain", health=10, mana=10, mana_regeneration_rate=1)

    def test_hero(self):
        self.assertEqual(Hero(name="Gosho", title="Ubiec", health=100, mana=100, mana_regeneration_rate=2), self.super_gosho)
        self.assertEqual(Hero(name="America", title="Captain", health=10, mana=10, mana_regeneration_rate=1), self.captain_america)

    def test_is_alive(self):
        self.assertEqual(self.super_gosho.is_alive(), True)
        self.assertEqual(self.captain_america.is_alive(), True)

    def test_get_HP(self):
        self.assertEqual(self.super_gosho.get_health(), 100)
        self.assertEqual(self.captain_america.get_health(), 10)

    def test_get_Mana(self):
        self.assertEqual(self.super_gosho.get_mana(), 100)
        self.assertEqual(self.captain_america.get_mana(), 10)

    def test_healing(self):
        self.super_gosho.take_damage(50)
        self.captain_america.take_damage(5)
        self.assertTrue(self.super_gosho.take_healing(10))
        self.assertTrue(self.captain_america.take_healing(1))
        self.assertEqual(self.super_gosho.get_health(), 60)
        self.assertEqual(self.captain_america.get_health(), 6)

    def test_cast(self):
        spell = Spell("Fireball", 30, 5, 2)
        self.assertTrue(self.captain_america.can_cast(spell))

    def test_is_equp(self):
        weapon = Weapon("Old pen", 1)
        self.assertTrue(self.captain_america.equip(weapon))

    def test_is_learned(self):
        spell = Spell("Fireball", 30, 5, 2)
        self.assertTrue(self.captain_america.learn(spell))

    # def test_attack(self):
    #     spell = Spell("Fireball", 30, 5, 2)
    #     self.captain_america.learn(spell)
    #     print(self.captain_america.attack("spell"))
    #     self.assertEqual(self.captain_america.attack("spell"), 30)


if __name__ == "__main__":
    unittest.main()
