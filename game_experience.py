from dungeon import *
from unit import *
from weapons_spells import *


class GamingExperiance:
	
	def __init__(self):
		self.dung = Dungeon() 
		self.begin_game()
		self.game_on = True
		while self.game_on:
			self.gaming_cycle()
			print(self.dung)
	
	def begin_game(self):
		h1 = input("Name your hero:")
		h2 = input("Give him a title:")
		h3 = input("Now some health:")
		h4 = input("Don't forget the mana:")
		h5 = input("Regenarating mana with:")
		self.dung.hero = Hero(h1, h2, h3, h4, h5)

	def gaming_cycle(self):
		inps = {"moves": ["down", "up", "left", "right"]}
		user_inp = input("What is thy bidding my master? ")
		if user_inp in inps["moves"]:
			self.dung.move_hero(user_inp)
		elif user_inp in ["help", "-help"]:
			print("\n" + 25*"=" + "\n" +
'''Use - down, up, left, right - to move

Use - help, -help - for help

Use - Hero - learn info 'bout yer hero\n''' + 25*"=" + "\n") 
		elif user_inp in ["exit", "exit()", "e"]:
			self.game_on = False


def main():
	g1 = GamingExperiance()
	

if __name__ == "__main__":
	main()
