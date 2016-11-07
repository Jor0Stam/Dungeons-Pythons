import unittest
from enemy import Enemy


class Test_enemy(unittest.TestCase):

    def setUp(self):
        self.sauron = Enemy(health=95, mana=50, damage=25)
        self.loki = Enemy(health=70, mana=80, damage=40)

    def test_enemy(self):
        self.assertEqual(Enemy(health=95, mana=50, damage=25), self.sauron)
        self.assertEqual(Enemy(health=70, mana=80, damage=40), self.loki)

    def test_get_HP(self):
        self.assertEqual(self.sauron.get_health(), 95)
        self.assertEqual(self.loki.get_health(), 70)

    def test_get_mana(self):
        self.assertEqual(self.sauron.get_mana(), 50)
        self.assertEqual(self.loki.get_mana(), 80)

    def test_healing(self):
        self.sauron.take_damage(50)
        self.loki.take_damage(50)
        self.assertTrue(self.sauron.take_healing(100))
        self.assertTrue(self.loki.take_healing(10))
        self.assertEqual(self.sauron.get_health(), 95)
        self.assertEqual(self.loki.get_health(), 30)

    def test_dying(self):
        self.sauron.take_damage(-1000)
        self.loki.take_damage(1000)
        self.assertFalse(self.sauron.is_alive())
        self.assertFalse(self.loki.is_alive())

    def test_attack(self):
        self.assertEqual(self.sauron.attack(), self.sauron.damage)


if __name__ == "__main__":
    unittest.main()
