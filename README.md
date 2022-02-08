# Dungeon_Hiro
Text-based dungeon game using nested while loops in Python

Tomas Donatelli Pitfield
Dungeon Hiro
Intro
“Dungeon Hiro” is a text based action game created in Python. The game starts off with the player entering their name and spawning on to a map with enemies and items. Each enemy, item, and the player spawn on a 10x10 grid with their location displayed as (x, y) coordinates. The player can then move around the map interacting with items and fighting enemies. The game ends when the player has either defeated the dragon or died fighting an enemy. The battle takes the player’s base damage plus any weapons equipped and displays a random attack damage within that range for each attack iteration until either the player or the enemy is dead (heath points < 0).

Design & Imp
	The game is built around nested while loops with user input to guide a decision tree with 6 options: 
Move. This option has the player call the move() method. Move() method is defined as a method of the hero object which is a child of the character parent object. Move() method uses a while loop to display the player’s current position and ask for user input to either move North (y+1), South (y-1), East (x+1), or West (x-1). This method then changes the player’s location vector (coordinates) and displays them to the user. This method has built in limits such that the player is not able to move beyond the 10x10 map. For instance, if the player’s location is (0, 0) they will be unable to move South or West.
Use Item. This option first checks the player location with the locations of the potions and weapons that were spawned at the beginning of the game. If the player is at the same location (coordinates) as an item, this option calls either the drink(item) or the equip(weapon) methods of the child hero object. If the item at the same location as the player is a potion, the drink(item) method is called adding the health points of whatever potion is at the same location to those of the player character. There are three potions at different, random locations of the map. If the item at the same location is a weapon, the equip(weapon) method is called, adding the damage points of the specific weapon to the player's damage points. There are three weapons at different, random locations of the map.
Battle. This option first checks to see which of the 4 enemies is at the same location as the player (if any). Then, it has the player call the battle(enemy) method of the parent Character object. The battle(enemy) method is very similar to the first python project of this module. Using a while loop, this method uses player damage to subtract health points from the enemy that is input as an argument. Then, it uses enemy damage to subtract health points from the player (self). Each attack has a random value for damage within a range based on the character’s (player or enemy) base damage and any weapons. The outcome is always different, due to random chance. The player is more likely to win if they have higher health from potions or higher damage from weapons, but the actual attack damage will change in every attack for every battle method. Once the health points of either the enemy or the player are < 0, then it breaks the loop.
Display. A print statement showing the player’s current health points and damage points.
Map. A series of print statements showing the spawn coordinates (different every time you play) of each of the enemies, potions, and weapons.
Exit. Exit the game.




