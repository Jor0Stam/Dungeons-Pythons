# BEGIN_GAME

CHOOSE_HERO = "Build your won hero or use one of ours?(Type new if you want to create your own hero) "
NEW_HERO = ["New Hero", "new"]
HERO_NAME = "Name your hero:"
HERO_TITLE = "Give him a title:"
HERO_HP = "Now some health:"
HERO_MP = "Don't forget the mana:"
HERO_MANA_REGEN = "Regenarating mana with:"

# FIGHT CLASS

INIT_FIGHT = "\nA fight is started between our {h} (health={hp}, mana={mp}) and Enemey(health={eh}, mana={em}, damage={ed})."
BATTLE_END = "\n{} is death!"

HERO_ATTACK_SPELL = "{hero} casts a {spell}, hits enemy for {dmg} dmg. Enemy health is {hp}."
HERO_ATTACK_WEAPON = "{hero} hits with {weapon}, hits enemy for {dmg} dmg. Enemy health is {hp}."
HERO_NO_ATTACK = "Our {hero} has no weapon, nor spell, that's way he will fail!"

ENEMY_ATTACK = "Enemy hits {hero} for {dmg} dmg. {hero} health is {hp}."
ENEMY_ATTACK_SPELL = "Enemy casts a {spell}, hits {hero} for {dmg} dmg. {hero} health is {hp}."
ENEMY_ATTACK_WEAPON = "Enemy hits with {weapon}, hits {hero} for {dmg} dmg. {hero} health is {hp}."

# GAME EXPERIANCE

BEGIN_GAME = "\nHello there.. I see you're interested in claiming your nerd status, so let's play :)"
GAME_OVER = "\nYou either die a hero, or live long enough to see yourself become the villian.\nSadly {hero} died a disturbing death. "
HELP_INFO = "\n" + 25 * "=" + "\n" +'''Use - <down>, <up>, <left>, <right> - to move

Use - <help> - for help

Use - <Hero> - learn info 'bout yer hero

Use - <exit> - to exit game\n''' + 25 * "=" + "\n"
HERO_INFO = "{hero} with {hp}hp and {mp}mana"
COMAND_ERROR = "This terminal reads only pure Elvish you Muggle! (Type <help> for... yeah you guesed right, Help!)"

# TREASURES

HERO_FOUND_HEAL = "\n{hero} found {hp} hp!"
HERO_FOUND_MANA = "\n{hero} found {mp} mp!"
HERO_FOUND_WEAPON = "\n{hero} picked {weapon}"
HERO_FOUND_SPELL = "\n{hero} learned {spell}"

# WEAPONS & SPELLS

WEAPON_INFO = "\n{name} that deals {dmg} damage points!"
SPELL_INFO = "\n{name} dealing {dmg} damage points, consuming {mp} mana. Can cast from {cr} range"

# DUNGEON

LAST_LVL = '''\n...While cleaning his wounds, our {hero} heard somebody coming.
It was the long lost princess of his kingdom.
She looked sad and lonely, and needed a strong hero to kiss her.
So he kissed her, took her to his place, they drank merlo, they listened to Bethoven and...

Now our hero is up for a new adventure!

If You Liked the Game don't hesitate and tell me that I am awesome and godLike:)'''
NOT_LAST_LVL = '''Our {hero} heard about a damsel in distress in the next cave,
which looked even more creepy than the current one.
To save type <I am afraid and I'll save like NOT the hero that I am>
Otherwise prepare for the lvl!'''
